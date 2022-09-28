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

###  A11y light

### A11y dark

Background color: ![#2b2b2b](https://via.placeholder.com/20/2b2b2b/2b2b2b.png) `#2b2b2b`

Highlight color: ![#ffd9001a](https://via.placeholder.com/20/ffd9001a/ffd9001a.png) `#ffd9001a`

**WCAG compliance**

| Color | Hex | Ratio | Normal text | Large text |
| ----- | --- | ----- | ----------- | ---------- |
| ![#d4d0ab](https://via.placeholder.com/20/d4d0ab/d4d0ab.png) | `#d4d0ab` | 9.04 : 1 | AAA | AAA |
| ![#ffa07a](https://via.placeholder.com/20/ffa07a/ffa07a.png) | `#ffa07a` | 7.12 : 1 | AAA | AAA |
| ![#f5ab35](https://via.placeholder.com/20/f5ab35/f5ab35.png) | `#f5ab35` | 7.25 : 1 | AAA | AAA |
| ![#ffd700](https://via.placeholder.com/20/ffd700/ffd700.png) | `#ffd700` | 10.09 : 1 | AAA | AAA |
| ![#abe338](https://via.placeholder.com/20/abe338/abe338.png) | `#abe338` | 9.29 : 1 | AAA | AAA |
| ![#00e0e0](https://via.placeholder.com/20/00e0e0/00e0e0.png) | `#00e0e0` | 8.59 : 1 | AAA | AAA |
| ![#dcc6e0](https://via.placeholder.com/20/dcc6e0/dcc6e0.png) | `#dcc6e0` | 8.9 : 1 | AAA | AAA |
| ![#f8f8f2](https://via.placeholder.com/20/f8f8f2/f8f8f2.png) | `#f8f8f2` | 13.28 : 1 | AAA | AAA |
| ![#ffd9001a](https://via.placeholder.com/20/ffd9001a/ffd9001a.png) | `#ffd9001a` | 10.23 : 1 | AAA | AAA |

## Tests

Just open a terminal and run,

```
python test/run_tests.py
```

You will see the results under `test/results` in html format.
