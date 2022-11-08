import ast
import os
from setuptools import setup, find_packages

from a11y_pygments.utils.utils import find_all_themes_packages


def find_entrypoints():
    themes = find_all_themes_packages()
    entrypoints = []
    base_package = 'a11y_pygments'
    for theme in themes:
        name = theme.replace('_', '-')
        package = '{}.{}.style:Theme'.format(base_package, theme)
        entrypoints.append('{} = {}'.format(name, package))
    print(entrypoints)
    return entrypoints


def get_long_description():
    with open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'README.md'
    ), encoding='utf8') as fp:
        return fp.read()


def get_version(module='a11y_pygments'):
    """Get version."""
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, module, '__init__.py')
    with open(path, 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


setup (
  name='accessible-pygments',
  version=get_version(),
  description='A collection of accessible pygments styles',
  long_description=get_long_description(),
  long_description_content_type='text/markdown',
  license='BSD',
  keywords='pygments style accessible a11',

  author='Stephannie Jimenez Gacha',
  author_email='steff456@hotmail.com',

  url='https://github.com/Quansight-Labs/accessible-pygments',

  packages=find_packages(),
  install_requires=[
    'pygments >= 1.5'
  ],

  entry_points ={
    "pygments.styles": find_entrypoints()
  },

  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)
