# Accessible pygments themes

[![conda version](https://img.shields.io/conda/vn/conda-forge/accessible-pygments?color=e27e8c&style=for-the-badge)](https://anaconda.org/conda-forge/accessible-pygments)
[![pip version](https://img.shields.io/pypi/v/accessible-pygments?color=63a6c8&style=for-the-badge)](https://pypi.org/project/accessible-pygments/)
[![conda-forge downloads](https://img.shields.io/conda/dn/conda-forge/accessible-pygments?label=conda-forge%20downloads&style=for-the-badge)](https://anaconda.org/conda-forge/accessible-pygments)
[![pip downloads](https://img.shields.io/pypi/dm/accessible-pygments?color=%23acc00d&label=PyPI%20downloads&style=for-the-badge)](https://pypi.org/project/accessible-pygments/)
[![demo](https://img.shields.io/badge/Demo-Click%20me!-blueviolet?style=for-the-badge)](https://quansight-labs.github.io/accessible-pygments/)

- [Accessible pygments themes](#accessible-pygments-themes)
  - [Accessibility details ♿️](#accessibility-details-️)
    - [WCAG 2.1 - AAA compliant](#wcag-21---aaa-compliant)
    - [WCAG 2.1 - AA compliant](#wcag-21---aa-compliant)
  - [Documentation 📖](#documentation-)
    - [Installation 💻](#installation-)
    - [Using the themes directly in your code or app](#using-the-themes-directly-in-your-code-or-app)
    - [Using the themes in your Sphinx documentation](#using-the-themes-in-your-sphinx-documentation)
  - [Development and contribution](#development-and-contribution)
  - [Acknowledgments 🤝](#acknowledgments-)
  - [License 📑](#license-)

This package includes a collection of accessible themes for pygments based on multiple open-source syntax highlighting themes. The images below show all the themes side by side.

![Display of all the light themes side by side](./docs/light_themes.png)

![Display of all dark themes side by side](./docs/dark_themes.png)

:sparkles: For a demo of all our themes please [visit our online demo](https://quansight-labs.github.io/accessible-pygments/) :sparkles:

## Accessibility details ♿️

> **Note**
> What do we mean by accessible? In this context we are specifically referring to themes which meet the [WCAG 2.1 criteria for color contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).
> Some themes included are also color-blind friendly.

### WCAG 2.1 - AAA compliant

The following themes are AAA compliant with [WCAG 2.1 criteria for color contrast](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html).

- [`a11y-dark`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/a11y_dark)
- [`a11y-high-contrast-dark`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/a11y_high_contrast_dark)
- [`pitaya-smoothie`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/pitaya_smoothie) - Color-blind friendly.
- [`github-light`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_light) - Color-blind friendly.
- [`github-dark`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_dark) - Color-blind friendly.
- [`github-light-colorblind`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_light_colorblind) - Color-blind friendly.
- [`github-dark-colorblind`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_dark_colorblind) - Color-blind friendly.
- [`github-light-high-contrast`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_light_high_contrast) - Color-blind friendly.
- [`github-dark-high-contrast`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/github_dark_high_contrast) - Color-blind friendly.
- [`gotthard-dark`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/gotthard-dark) - Color-blind friendly.

### WCAG 2.1 - AA compliant

The following themes are AA compliant with [WCAG 2.1 criteria for color contrast](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html).

- [`a11y-light`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/a11y_light)
- [`a11y-high-contrast-light`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/a11y_high_contrast_light)
- [`gotthard-light`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/gotthard-light) - Color-blind friendly.
- [`blinds-light`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/blinds-light) - Color-blind friendly.
- [`blinds-dark`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/blinds-dark) - Color-blind friendly.
- [`greative`](https://github.com/Quansight-Labs/accessible-pygments/tree/main/a11y_pygments/greative) - Accessible to most forms of colorblindness and low light settings.

## Documentation 📖

### Installation 💻

`accessible-pygments` is available through pip and conda.

You can install it through the following commands:

```bash
conda install -c conda-forge accessible-pygments

# if you prefer using mamba
mamba install -c conda-forge accessible-pygments
```

```bash
pip install accessible-pygments
```

If you prefer to install the themes directly from the source:

```bash
# clone the repository
git clone git@github.com:Quansight-Labs/accessible-pygments.git
cd accessible-pygments

pip install .
```

### Using the themes directly in your code or app

If you want to directly use the themes in your code, you can do so by importing the theme and passing it to the `style` argument of the `HtmlFormatter` class.

```python
from pygments.formatters import HtmlFormatter
HtmlFormatter(style='a11y-light').style
<class 'accessible-pygments.A11yLight'>
```

### Using the themes in your Sphinx documentation

1. You will need to add `accessible-pygments` as a dependency to your documentation:

   ```toml
   # for example if using a pyproject.toml file
   dependencies=["accessible-pygments"]
   ```

2. Modify your `conf.py` file to specify the `accessible-pygments` style:

   ```python
   "pygments_style": "a11y-light"
   ```

3. Build your documentation as usual.

## Development and contribution

You can find our contribution guides on [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments 🤝

We want to thank the following sources for being the source of inspiration for one or more themes that are available in this repository,

- [a11y dark and light syntax highlighting](https://github.com/ericwbailey/a11y-syntax-highlighting).
- [pitaya smoothie VSCode theme](https://github.com/trallard/pitaya_smoothie).
- [github VSCode themes](https://github.com/primer/github-vscode-theme).
- [gotthard VSCode themes](https://github.com/janbiasi/vscode-gotthard-theme/).
- [blinds VSCode themes](https://github.com/orbulant/blinds-theme).
- [greative VSCode theme](https://github.com/SumanKhdka/Greative-vscode-Theme).

## License 📑

`accessible-pygments` is licensed under the [OSI BSD-3 Clause license](./LICENSE).
