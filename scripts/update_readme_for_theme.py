import logging
from argparse import ArgumentParser
from importlib import import_module
from inspect import getdoc
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pygments.styles import get_style_by_name

from a11y_pygments.utils.utils import find_all_themes_packages
from a11y_pygments.utils.wcag_contrast import (
    contrast_ratio,
    get_wcag_level_large_text,
    get_wcag_level_normal_text,
    hex_to_rgb,
    hexstr_without_hash,
)

# This script generates READMEs for themes from their style.py definitions

HERE = Path(__file__).parent
REPO = HERE.parent

env = Environment(
    loader=FileSystemLoader(HERE / "templates"), autoescape=select_autoescape()
)


def update_readme(theme):
    """Given a theme module name, update that theme's README file on disk"""

    # Get the theme colors
    theme_style_module = import_module(f"a11y_pygments.{theme}.style")
    color_cls = theme_style_module.Colors
    theme_cls = theme_style_module.Theme
    theme_kebab_case = theme.replace("_", "-")
    style = get_style_by_name(theme_kebab_case)

    # Calculate contrast ratios and WCAG ratings for all foreground colors
    foreground_colors = []
    for key in vars(color_cls):
        value = getattr(color_cls, key)
        if not callable(value) and not key.startswith("__"):
            contrast = contrast_ratio(
                hex_to_rgb(value), hex_to_rgb(style.background_color)
            )
            foreground_colors.append(
                {
                    "hex": hexstr_without_hash(value),
                    "contrast_ratio": round(contrast, 1),
                    "rating_normal_text": get_wcag_level_normal_text(contrast),
                    "rating_large_text": get_wcag_level_large_text(contrast),
                }
            )

    # Render the README template with the contrast info
    template = env.get_template("readme.md")
    result = template.render(
        theme=theme_kebab_case,
        theme_title=theme.replace("_", " ").title(),
        theme_docstring=getdoc(theme_cls),
        background_hex=hexstr_without_hash(style.background_color),
        highlight_hex=hexstr_without_hash(style.highlight_color),
        colors_hex=foreground_colors,
    )

    # Save the new README file
    out = REPO / "a11y_pygments" / theme / "README.md"
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
        update_readme(args.theme)
    else:
        # Update all theme READMEs
        for theme in themes:
            update_readme(theme)
