from setuptools import setup, find_packages

setup (
  name='accessible-pygments',
  version='0.0.0',
  description='A Collection of Accessible Pygments Styles',
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
    "pygments.styles": ["a11-light = a11-pygments.a11-light:A11LightStyle"]
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
