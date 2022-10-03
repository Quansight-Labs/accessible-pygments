# Accessible pygments themes

This package includes a collection of accessible themes for pygments based on different sources.

Our current themes include,

- `a11y-light`
- `a11y-dark`
- `a11y-light-high-contrast`
- `a11y-dark-high-contrast`

## Installation

Just open a terminal and run,

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
