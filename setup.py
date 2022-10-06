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


setup (
  name='accessible-pygments',
  version='0.0.1',
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
