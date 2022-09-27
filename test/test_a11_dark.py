import os
import os.path as osp

from pygments import highlight as pygments_highlight
#from pygments.lexers import JavascriptLexer
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

actdir = osp.dirname(__file__)
name = osp.join(actdir, 'test.py')

with open(name, 'r') as f:
    lines = f.read()

lexer = get_lexer_by_name("python", stripall=True)
style = get_style_by_name('a11-dark')
formatter = HtmlFormatter(style=style, full=True)

result = pygments_highlight(lines, lexer, formatter)

with open('result.html', 'w') as f:
    f.write(result)
