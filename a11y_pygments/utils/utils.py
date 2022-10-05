import os.path as osp

from setuptools import find_packages
from typing import List

from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
from pygments.token import Text


def find_all_themes_packages() -> List[ str ]:
    """Finds the current supported themes in the a11y pygments package."""
    exclude = { 'test', 'a11y_pygments', 'a11y_pygments.utils' }
    packages = set( find_packages() )
    themes = list( packages - exclude )
    themes = [ x.split( '.' )[ 1 ] for x in themes ]
    return themes


def find_all_themes() -> List[ str ]:
    """Finds the current supported themes names in the a11y pygments package."""
    exclude = { 'test', 'a11y_pygments', 'a11y_pygments.utils' }
    packages = set( find_packages() )
    themes = list( packages - exclude )
    themes = [ x.split( '.' )[ 1 ] for x in themes ]
    themes = [ x.replace('_', '-') for x in themes ]
    return themes


def generate_css(themes: List[ str ]):
    """Generate css for the given themes."""
    basedir = 'a11y_pygments'
    for theme in themes:
        style = get_style_by_name( theme )
        formatter = HtmlFormatter( style=style, full=True )
        css = formatter.get_style_defs()
        css += "\n .highlight { background: %s; color: %s; }"%(
            style.background_color, style.styles[Text]
        )
        print(style.background_color, style.styles[Text])
        package = theme.replace('-', '_')
        out = osp.join( basedir, package, 'style.css' )
        with open( out, 'w' ) as f:
            f.write( css )
