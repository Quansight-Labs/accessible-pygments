import os
import os.path as osp

from pygments import highlight as pygments_highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


languages = {
    "python": "py",
    "javascript": "js",
    "bash": "bash",
    "html": "html",
    "css": "css",
    "markdown": "md",
    }

themes = [
    "a11y-light",
    "a11y-dark",
    "a11y-dark-high-contrast",
    "a11y-light-high-contrast",
    "pitaya-smoothie"
    ]

actdir = osp.dirname(__file__)
outdir = osp.join(actdir, 'results')

if not osp.exists(outdir):
    os.mkdir(outdir)

for language in languages:
    ext = languages[language]
    name = osp.join(actdir, 'scripts', 'test.' + ext)

    with open(name, 'r') as f:
        lines = f.read()

    lexer = get_lexer_by_name(language, stripall=True)

    for theme in themes:
        style = get_style_by_name(theme)
        formatter = HtmlFormatter(style=style, full=True)
        result = pygments_highlight(lines, lexer, formatter)
        the_css = formatter.get_style_defs()

        theme_outdir = osp.join(outdir, theme)

        if not osp.exists(theme_outdir):
            os.mkdir(theme_outdir)

        out = osp.join(theme_outdir, ext + '.html')
        with open(out, 'w') as f:
            f.write(result)

        with open(osp.join(theme_outdir, ext + '.css'), 'w') as f:
            f.write(the_css)
