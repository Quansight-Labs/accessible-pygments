"""
Script to create individual HTML samples for each of the themes in accessible-pygments.

Usage::

    python test/render_html.py
"""
import os
from pathlib import Path

from pygments import highlight as pygments_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name

from a11y_pygments.utils.utils import get_themes_names

# List of available language examples
languages = {
    "python": "py",
    "javascript": "js",
    "bash": "bash",
    "html": "html",
    "css": "css",
    "markdown": "md",
}

# Top-level package directory
pkg_dir = Path(__file__).parent.parent
# Output directory for the HTML files
outdir = pkg_dir / "test" / "html-files"
# Language sample scripts
samples_dir = pkg_dir / "tools" / "sample-scripts"


def render_html(themes: list, languages=languages, outdir=outdir):
    """Generate rendered HTML sample of the themes for the specified languages.

    Args:
        themes (list): list of registred themes.
        languages (dict, optional): Dict containing the languages samples to render.
            Defaults to languages.
        outdir (pathlib.Path, optional): Directory to save the rendered HTML files to.
            Defaults to outdir.
    """

    if not outdir.exists():
        os.mkdir(outdir)

    for language in languages:
        ext = languages[language]
        file_name = samples_dir / f"test.{ext}"

        with open(file_name, "r") as f:
            lines = f.read()

        lexer = get_lexer_by_name(language, stripall=True)

        for theme in themes:
            style = get_style_by_name(theme)
            formatter = HtmlFormatter(style=style, full=True, hl_lines=[2, 3, 4])
            result = pygments_highlight(lines, lexer, formatter)

            theme_outdir = outdir / theme

            if not theme_outdir.exists():
                os.mkdir(theme_outdir)

            out_file = theme_outdir / f"{ext}.html"
            with open(out_file, "w") as f:
                f.write(result)


if __name__ == "__main__":
    # get names of all themes
    themes = get_themes_names()
    render_html(themes)
