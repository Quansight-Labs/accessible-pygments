# Accessible pygments themes

Pygments accessible themes based on [a11y dark and light syntax highlighting](https://github.com/ericwbailey/a11y-syntax-highlighting).

Our current themes include,

- `a11y-light`
- `a11y-dark`

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

## Themes
The current themes available include,

-   **A11y light**

-   **A11y dark**

## Tests

Just open a terminal and run,

```
python test/run_tests.py
```

You will see the results under `test/results` in html format.
