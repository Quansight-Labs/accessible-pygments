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


def contrast_markdown_table(color_contrasts):
    header_row = ["Color", "Hex", "Ratio", "Normal text", "Large text"]

    # Initialize column widths with character counts from the header row
    column_widths = [len(header) for header in header_row]

    # Create rows and update column width based on longest cell within a column
    rows = []
    for cc in color_contrasts:
        row = [
            f"![#{cc['hex']}](https://via.placeholder.com/20/{cc['hex']}/{cc['hex']}.png)",
            f"`#{cc['hex']}`",
            f"{cc['contrast_ratio']} : 1",
            f"{cc['wcag_level_normal_text']}",
            f"{cc['wcag_level_large_text']}",
        ]
        rows.append(row)

        # Column widths must be equal to the widest cell in the column, so
        # iterate through cells in row and update column widths if necessary
        for i, cell in enumerate(row):
            if len(cell) > column_widths[i]:
                column_widths[i] = len(cell)

    lines = []

    # Table header line
    lines.append(
        "| "
        + " | ".join(
            header.ljust(width) for header, width in zip(header_row, column_widths)
        )
        + " |"
    )

    # Separator line
    lines.append("| " + " | ".join("-" * width for width in column_widths) + " |")

    for row in rows:
        # Single row in table
        lines.append(
            "| "
            + " | ".join(cell.ljust(width) for cell, width in zip(row, column_widths))
            + " |"
        )

    return "\n".join(lines)


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

    # Calculate contrast ratios and WCAG ratings for all foreground colors
    foreground_colors = {}
    for key in vars(color_cls):
        value = getattr(color_cls, key)
        if not callable(value) and not key.startswith("__"):
            if value in foreground_colors:
                continue
            contrast = contrast_ratio(
                hex_to_rgb(value), hex_to_rgb(style.background_color)
            )
            foreground_colors[value] = {
                "hex": hexstr_without_hash(value),
                "contrast_ratio": round(contrast, 1),
                "wcag_level_normal_text": get_wcag_level_normal_text(contrast),
                "wcag_level_large_text": get_wcag_level_large_text(contrast),
            }

    # Render the README template with the contrast info
    with open(HERE / "templates" / "README.md", "r") as file:
        template_str = file.read()
    template = string.Template(template_str)
    result = template.substitute(
        theme=theme_kebab_case,
        theme_title=theme.replace("_", " ").title(),
        theme_docstring=getdoc(theme_cls),
        background_hex=hexstr_without_hash(style.background_color),
        highlight_hex=hexstr_without_hash(style.highlight_color),
        contrast_table=contrast_markdown_table(foreground_colors.values()),
    )

    # Save the new README file
    out = REPO / "a11y_pygments" / theme / "README.md"
    with open(out, "w") as f:
        logging.info("Updating %s", out)
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
