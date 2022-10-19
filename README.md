# Accessible pygments themes

![conda version](https://img.shields.io/conda/vn/conda-forge/accessible-pygments?color=e27e8c&style=for-the-badge)  ![pip version](https://img.shields.io/pypi/v/accessible-pygments?color=63a6c8&style=for-the-badge)  ![conda-forge downloads](https://img.shields.io/conda/dn/conda-forge/accessible-pygments?label=conda-forge%20downloads&style=for-the-badge)  ![pip downloads](https://img.shields.io/pypi/dm/accessible-pygments?color=%23acc00d&label=PyPI%20downloads&style=for-the-badge)

This package includes a collection of accessible themes for pygments based on different sources.

Our current themes include,

- `a11y-light`
- `a11y-dark`
- `a11y-high-contrast-light`
- `a11y-high-contrast-dark`
- `pitaya-smoothie`
- `github-light`
- `github-dark`
- `github-light-colorblind`
- `github-dark-colorblind`

## Installation

Our package is available in both conda and pip via,

```
conda install -c conda-forge accessible-pygments
```

```
pip install accessible-pygments
```

If you want to install it directly from source,

```
git clone git@github.com:Quansight-Labs/accessible-pygments.git
cd accessible-pygments
pip install .
```

## Usage

Import it using the name identifier for the desired theme,

```
from pygments.formatters import HtmlFormatter
HtmlFormatter(style='a11y-light').style
<class 'accessible-pygments.A11yLight'>
```

## Tests

Just open a terminal and run,

```
python test/run_tests.py
```

You will see the results under `test/results` in html format for each supported theme.


## Acknowledgements

We want to thank the following sources for being the source of inspiration of one or more themes that are available in this repository,

- [a11y dark and light syntax highlighting](https://github.com/ericwbailey/a11y-syntax-highlighting).
