# Copyright (c) Quansight Labs.
# Distributed under the terms of the Modified BSD License.

"""
Script to generate the css files for the themes in accessible-pygments.

Usage::

    python tools/run_css.py
    python tools/run_css.py --save-file <output directory>

"""
import argparse
import logging
from pathlib import Path

from a11y_pygments.utils.utils import generate_css, get_themes_names

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save-dir", type=str, default="", help="Directory to save the css files"
    )
    args = parser.parse_args()

    if args.save_dir:
        save_dir = Path(args.save_dir).resolve()
        logging.info(f"Saving css files to {save_dir}")

    themes = get_themes_names()
    generate_css(themes, args.save_dir)
