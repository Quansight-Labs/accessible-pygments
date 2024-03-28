# Contributing to accessible pygments themes

Welcome! And thanks for taking your time to contribute to this project 🤩

- [Contributing to accessible pygments themes](#contributing-to-accessible-pygments-themes)
  - [Submit an issue 📬](#submit-an-issue-)
  - [Contributing to this package](#contributing-to-this-package)
    - [Pre-requisites 📦](#pre-requisites-)
    - [Creating your development environment 👩🏻‍💻 👨🏼‍💻](#creating-your-development-environment--)
    - [Running the tests](#running-the-tests)
    - [Rendering the HTML examples](#rendering-the-html-examples)
    - [Linting and formatting](#linting-and-formatting)
  - [Adding a new theme 🎨](#adding-a-new-theme-)
    - [Where to add a new theme 👩🏼‍🎨](#where-to-add-a-new-theme-)
    - [Customize your `style.py` file](#customize-your-stylepy-file)
    - [Visualize and debug your theme](#visualize-and-debug-your-theme)
    - [Update the `README.md` file](#update-the-readmemd-file)
      - [Add your theme to our static page](#add-your-theme-to-our-static-page)
    - [Create a Pull Request](#create-a-pull-request)

## Submit an issue 📬

Please share your thoughts on fixes and features [in the issue tracker](https://github.com/Quansight-Labs/accessible-pygments/issues).
When doing so, add a clear description, and provide as much information as possible about your environment.

## Contributing to this package

### Pre-requisites 📦

You will need to have the following installed locally:

- `git`
- Python >= 3.9
- [hatch](https://hatch.pypa.io/)

### Creating your development environment 👩🏻‍💻 👨🏼‍💻

1. Fork this repository to your GitHub account, then clone it to your local machine:

   ```bash
    git clone https://github.com/<your-username>/accessible-pygments.git
   ```

   Remember that this fork is a copy of the repository and any changes in it don't affect the original one.

2. From here you can create your local environments with hatch:

   ```bash
    hatch env create
   ```

3. You can verify that the environment was created successfully by running:

   ```console
    $ hatch env show
   ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
   ┃ Name    ┃ Type    ┃ Dependencies ┃ Scripts           ┃
   ┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
   │ default │ virtual │              │                   │
   ├─────────┼─────────┼──────────────┼───────────────────┤
   │ dev     │ virtual │              │ css               │
   │         │         │              │ render_html       │
   |         |         |              | update_theme_docs |
   ├─────────┼─────────┼──────────────┼───────────────────┤
   │ test    │ virtual │ hypothesis   │ tests             │
   │         │         │ pytest       │                   │
   └─────────┴─────────┴──────────────┴───────────────────┘
   ```

### Running the tests

You can run the tests directly with hatch:

```bash
hatch run test:tests
```

### Rendering the HTML examples

You can generate individual HTML files for each of the themes included in `accessible_pygments` by running:

```bash
hatch run dev:render_html
```

This will add the HTML files under `docs/` for each supported theme.
We recommend using your favorite browser to see the rich HTML output.

### Linting and formatting

We use several linters and formatters to ensure the code is consistent and clean.
You can run this with:

```bash
hatch run dev:lint
```

## Adding a new theme 🎨

### Where to add a new theme 👩🏼‍🎨

Our package is divided by themes, where each folder has the style of each theme, a description in Markdown and the source CSS file.

```text
├── a11y_pygments
│   ├── a11y_dark
│   │   ├── style.py
│   │   ├── style.css
│   │   ├── README.md
│   ├── a11y_light
│   │   ├── style.py
│   │   ├── style.css
│   │   ├── README.md
```

To add a new theme, please create a folder with your new theme name, like `white-cats` and add the three files
described before (so that it matches the rest of the themes).

### Customize your `style.py` file

You can use as a base one of our existing themes, this file needs to define a new class named `Theme` with the new colors and rules you want.

> **NOTE** 📝
> Please try to encapsulate all the raw colors in the `Colors` `enum` and call them in the rules section.
> This will help us with maintenance 🙏.

### Visualize and debug your theme

While working on your theme, it might be helpful to generate example HTML files with the following command:

```bash
hatch run dev:render_html
```

The HTML files are generated from sample source code files located under `tests/scripts`.

If successful, you should be able to see the results of your new theme applied to those code files under `docs/_build/<your-theme>`.

If you prefer to inspect the CSS separately from the HTML, use the following command:

```bash
hatch run dev:create_css
```

This will add the CSS file under `docs/_build/css/<your-theme>.css`.

### Update the `README.md` file

Once you are happy with the colors and the rules in the style file, please update the README for your new theme! You can generate a README with the following command:

```bash
hatch run dev:update_theme_docs your_theme_module_name
```

This script will:

- generate a table of contrast ratios of the colors you've chosen and their compliance with WCAG,
- pull the docstring from the `Theme` class and put it in the README as the description for your theme (if you are porting a theme or color
  palette developed elsewhere please acknowledge your source(s) in the docstring of the `Theme` class),
- take a screenshot of your theme applied to a code sample, save it at `a11y_pygments/<your_theme>/images/<your_theme>.png`, and embed it in the theme README.

Also, don't forget to add the name of your theme to our list of supported themes in the [main README](README.md).

#### Add your theme to our static page

We have a demo page where you will be able to change the style of different languages at the same time.
To add your new theme:

1. Open the `[docs/index.html](docs/index.html)` file.
2. Add your new theme name to the `themes` section:

With this change, you will be able to open `docs/index.html` in your favorite browser and find your new theme in our demo!

### Create a Pull Request

Once you have added and verified your theme you should be ready to open a Pull Request 👏🏻
