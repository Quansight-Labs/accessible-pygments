import logging
from argparse import ArgumentParser
from importlib import import_module
from inspect import getdoc
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright
from pygments.styles import get_style_by_name

from a11y_pygments.utils.utils import find_all_themes_packages
from a11y_pygments.utils.wcag_contrast import (
    contrast_ratio,
    get_wcag_level_large_text,
    get_wcag_level_normal_text,
    hex_to_rgb,
    hexstr_without_hash,
)
from tests.render_html import outdir as html_outdir
from tests.render_html import render_html

# This script generates READMEs for themes from their style.py definitions

HERE = Path(__file__).parent
REPO = HERE.parent

env = Environment(
    loader=FileSystemLoader(HERE / "templates"), autoescape=select_autoescape()
)


def contrast_by_foreground_color(color_cls, background_color: str):
    """Calculate contrast ratios and WCAG ratings for all foreground colors

    :param color_cls: A mapping of color names to six-value hex CSS color
        strings, the mapping comes from a class named Colors defined in
        <theme-name>/style.py
    :type color_cls: class object
    :param str background_color: Theme default background color for code blocks
        in six-value #RRGGBB hex format; for example white would be "#ffffff"
        (case insensitive)
    """
    foreground_colors = {}
    for key in vars(color_cls):
        value = getattr(color_cls, key)
        if not callable(value) and not key.startswith("__"):
            if value in foreground_colors:
                continue
            contrast = contrast_ratio(hex_to_rgb(value), hex_to_rgb(background_color))
            foreground_colors[value] = {
                "hex": hexstr_without_hash(value),
                "contrast_ratio": round(contrast, 1),
                "wcag_level_normal_text": get_wcag_level_normal_text(contrast),
                "wcag_level_large_text": get_wcag_level_large_text(contrast),
            }
    return foreground_colors


def update_readme(theme):
    """Given a theme module name, update that theme's README file on disk"""

    theme_kebab_case = theme.replace("_", "-")
    outdir = REPO / "a11y_pygments" / theme

    # Take a screenshot of the theme applied to a sample bash script
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 620, "height": 720})
        bash_sample_rendered_html = html_outdir / theme_kebab_case / "bash.html"
        page.goto("file://" + bash_sample_rendered_html.absolute().as_posix())
        page.screenshot(path=outdir / "images" / f"{theme_kebab_case}.png")
        browser.close()

    # Get the theme colors
    theme_style_module = import_module(f"a11y_pygments.{theme}.style")
    color_cls = theme_style_module.Colors  # access to foreground colors
    theme_cls = theme_style_module.Theme  # access to docstring
    style = get_style_by_name(
        theme_kebab_case
    )  # access to background and highlight colors

    # Render the README template with the contrast info
    template = env.get_template("README.md")
    result = template.render(
        theme=theme_kebab_case,
        theme_title=theme.replace("_", " ").title(),
        theme_docstring=getdoc(theme_cls),
        background_hex=hexstr_without_hash(style.background_color),
        highlight_hex=hexstr_without_hash(style.highlight_color),
        colors_hex=contrast_by_foreground_color(color_cls, style.background_color),
    )

    # Save the new README file
    out = outdir / "README.md"
    with open(out, "w") as f:
        logging.info(f"Updating {out}")
        f.write(result)


# You can either update one theme README at a time or all of them at once
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--theme",
        type=str,
        default="",
        help="Name of theme to update (example: a11y_dark)",
    )
    args = parser.parse_args()

    themes = find_all_themes_packages()

    if args.theme:
        # Update one theme README
        assert (
            args.theme in themes
        ), "Invalid theme (did you forget to use an underscore _ instead of a hyphen -?)"
        render_html(args.theme.replace("_", "-"))
        update_readme(args.theme)
    else:
        # Update all theme READMEs
        render_html()
        for theme in themes:
            update_readme(theme)
