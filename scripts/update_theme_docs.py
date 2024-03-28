import logging
import string
from argparse import ArgumentParser
from importlib import import_module
from inspect import getdoc
from pathlib import Path

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


def markdown_table(rows):
    # Calculate the maximum width of each column
    column_widths = [max(len(cell) for cell in column) for column in zip(*rows)]
    lines = []
    for row in rows:
        lines.append(
            "| "
            + " | ".join(cell.ljust(width) for cell, width in zip(row, column_widths))
            + " |"
        )
    separator = "| " + " | ".join("-" * width for width in column_widths) + " |"
    # Insert the separator row between the header row and the body rows
    lines.insert(1, separator)
    return "\n".join(lines)


def contrast_markdown_table(color_cls, background_color):
    rows = [["Color", "Hex", "Ratio", "Normal text", "Large text"]]

    # Calculate contrast ratios and WCAG ratings for all foreground colors
    unique_colors = set()
    for key in vars(color_cls):
        value = getattr(color_cls, key)
        if (
            not callable(value)
            and not key.startswith("__")
            and value not in unique_colors
        ):
            unique_colors.add(value)
            contrast = contrast_ratio(hex_to_rgb(value), hex_to_rgb(background_color))
            rrggbb = hexstr_without_hash(value)
            rows.append(
                [
                    # Color
                    f"![#{rrggbb}](https://via.placeholder.com/20/{rrggbb}/{rrggbb}.png)",
                    # Hex
                    f"`#{rrggbb}`",
                    # Ratio
                    f"{round(contrast, 1)} : 1",
                    # Normal text
                    get_wcag_level_normal_text(contrast),
                    # Large text
                    get_wcag_level_large_text(contrast),
                ]
            )

    return markdown_table(rows)


def update_readme(theme):
    """Given a theme module name, update that theme's README file on disk"""

    # Get the theme colors
    theme_style_module = import_module(f"a11y_pygments.{theme}.style")
    color_cls = theme_style_module.Colors  # access to foreground colors
    theme_cls = theme_style_module.Theme  # access to docstring
    theme_kebab_case = theme.replace("_", "-")
    style = get_style_by_name(
        theme_kebab_case
    )  # access to background and highlight colors

    # Render the README template with the contrast info
    with open(HERE / "templates" / "theme_readme.md", "r") as file:
        template_str = file.read()
    template = string.Template(template_str)
    result = template.substitute(
        theme=theme_kebab_case,
        theme_title=theme.replace("_", " ").title(),
        theme_docstring=getdoc(theme_cls),
        background_hex=hexstr_without_hash(style.background_color),
        highlight_hex=hexstr_without_hash(style.highlight_color),
        contrast_table=contrast_markdown_table(color_cls, style.background_color),
    )

    # Save the new README file
    out = REPO / "a11y_pygments" / theme / "README.md"
    with open(out, "w") as f:
        logging.info("Updating %s", out)
        f.write(result)


# You can either update one theme README at a time or all of them at once
if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Update theme readme",
        description="Updates the README.md file for themes in the accessible-pygments repo",
    )
    parser.add_argument(
        "themes", nargs="*", help="Name(s) of theme(s) to update (example: a11y_dark)"
    )
    args = parser.parse_args()

    # Check that each theme provided on the command line is a known theme. If
    # not, error and exit immediately
    all_themes = find_all_themes_packages()
    for theme in args.themes:
        assert (
            theme in all_themes
        ), "Invalid theme (did you forget to use an underscore _ instead of a hyphen -?)"

    # Update themes provided or, if none provided, update all themes in the repo
    themes = args.themes or all_themes
    for theme in themes:
        update_readme(theme)
