"""
Script to generate the css files for the themes in accessible-pygments.

Usage::

    python test/run_css.py
"""
from a11y_pygments.utils.utils import generate_css, get_themes_names

if __name__ == "__main__":
    themes = get_themes_names()
    generate_css(themes)
