import logging
import os
from pathlib import Path
from typing import List

from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
from pygments.token import Text
from setuptools import find_packages


def find_all_themes_packages() -> List[str]:
    """Finds the currently supported themes in the a11y_pygments package.

    Returns:
        themes: list of themes under the a11y_pygments package
    """
    exclude = {"test", "scripts", "a11y_pygments", "a11y_pygments.utils"}
    packages = set(find_packages())
    themes = list(packages - exclude)
    # drop the a11y_pygments part of the pkg name
    themes = [x.split(".")[1] for x in themes]
    return themes


def get_themes_names() -> List[str]:
    """Get themes names from the a11y_pygments package.

    Returns:
        themes: list of themes names
    """
    themes = find_all_themes_packages()
    themes = [x.replace("_", "-") for x in themes]
    logging.info(f"Found pygment themes: {themes}")
    return themes


def generate_css(themes: List[str], save_dir=""):
    """Generate css for the available themes.
    Args:
        themes (list): list of themes names
    """
    basedir = "a11y_pygments"
    for theme in themes:
        style = get_style_by_name(theme)
        formatter = HtmlFormatter(style=style, full=True, hl_lines=[2, 3, 4])
        css = formatter.get_style_defs()
        color = style.style_for_token(Text)["color"]
        css += (
            f"\n.highlight {{ background: {style.background_color}; color: #{color}; }}"
        )
        package = theme.replace("-", "_")

        if save_dir:
            if not Path(save_dir).joinpath("css").exists():
                os.mkdir(Path(save_dir).joinpath("css"))
            if "docs" in save_dir:
                out = Path(save_dir).joinpath("css", f"{package}-style.css")
            else:
                out = Path(save_dir) / package / "style.css"
        else:
            out = Path(basedir) / package / "style.css"

        logging.info(f"Saving css to {out}")
        with open(out, "w") as f:
            f.write(css)
