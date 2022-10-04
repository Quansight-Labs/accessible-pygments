from setuptools import setup, find_packages

setup (
  name='accessible-pygments',
  version='0.0.1',
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
    "pygments.styles": [
        "a11y-light = a11y_pygments.a11y_light.a11y_light:A11yLightStyle",
        "a11y-dark = a11y_pygments.a11y_dark.a11y_dark:A11yDarkStyle",
        "a11y-dark-high-contrast = a11y_pygments.a11y_high_contrast_dark.a11y_high_contrast_dark:A11yHighContrastDarkStyle",
        "a11y-light-high-contrast = a11y_pygments.a11y_high_contrast_light.a11y_high_contrast_light:A11yHighContrastLightStyle",
        "pitaya-smoothie = a11y_pygments.pitaya_smoothie.pitaya_smoothie:PitayaSmoothieStyle",
        ]
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
