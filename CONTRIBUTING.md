# Contributing to accessible pygments themes

Welcome! And thanks for taking your time to contribute to this project 🤩

- [Contributing to accessible pygments themes](#contributing-to-accessible-pygments-themes)
  - [Submit an issue 📬](#submit-an-issue-)
  - [Contributing to this package](#contributing-to-this-package)
    - [Pre-requisites 📦](#pre-requisites-)
    - [Creating your development environment 👩🏻‍💻 👨🏼‍💻](#creating-your-development-environment--)
    - [Running the tests](#running-the-tests)
    - [Rendering the HTML examples](#rendering-the-html-examples)
  - [Adding a new theme 🎨](#adding-a-new-theme-)
    - [1. Where to add a new theme 👩🏼‍🎨](#1-where-to-add-a-new-theme-)
    - [2. Customize your `style.py` file](#2-customize-your-stylepy-file)
    - [3. Visualize and debug your theme](#3-visualize-and-debug-your-theme)
    - [4. Update the `README.md` file for your theme](#4-update-the-readmemd-file-for-your-theme)
    - [5. Generate the source `style.css` file](#5-generate-the-source-stylecss-file)
    - [6. Add your theme to our static page](#6-add-your-theme-to-our-static-page)
    - [7. Create a Pull Request](#7-create-a-pull-request)

## Submit an issue 📬

Please share your thoughts for fixes and features [in the issue tracker](https://github.com/Quansight-Labs/accessible-pygments/issues).
When doing so, add a clear description, and please provide as much information as possible about your environment (Sphinx, pygments, and accessible-pygments versions).

## Contributing to this package

### Pre-requisites 📦

You will need to have the following installed locally:

- `git`
- Python >= 3.9
- [hatch](https://hatch.pypa.io/) - this is our recommended install method, but you can use conda instead.

### Creating your development environment 👩🏻‍💻 👨🏼‍💻

1. Fork the [`accessible-pygments`](https://github.com/Quansight-Labs/accessible-pygments) repository to your GitHub account, then clone it to your local machine:

   ```bash
    git clone https://github.com/<your-username>/accessible-pygments.git
   ```

   Remember that this fork is a copy of the repository and any changes in it doesn't affect the original one.

2. Create a new branch to add your changes to:

   ```bash
   git checkout -b <your-username>/<descriptive-name>
   ```

3. From here you can create your local environments with hatch:

   ```bash
    hatch env create
   ```

4. You can verify that the environment was created successfully by running:

   ```console
    $ hatch env show
   ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
   ┃ Name    ┃ Type    ┃ Dependencies ┃ Scripts     ┃
   ┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
   │ default │ virtual │              │             │
   ├─────────┼─────────┼──────────────┼─────────────┤
   │ dev     │ virtual │              │ css         │
   │         │         │              │ render_html │
   ├─────────┼─────────┼──────────────┼─────────────┤
   │ test    │ virtual │ hypothesis   │ tests       │
   │         │         │ pytest       │             │
   └─────────┴─────────┴──────────────┴─────────────┘
   ```

🎉 After running these instructions you will have an environment named `a11y-pygments-dev`, with a development version of the package installed.

> **Note**
> If you want to delete your local environments you can do this with the `hatch env prune` command

---

Alternatively you can use conda to create your environment manually:

```bash
conda create -n a11y-pygments-dev python=3.9
conda activate a11y-pygments-dev
pip install -e .
```

---

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

This will add the HTML files under `test/results` for each supported theme.
We recommend using your favorite browser to see the rich HTML output.

## Adding a new theme 🎨

### 1. Where to add a new theme 👩🏼‍🎨

Our package is divided by themes, where each folder inside the [`a11y_pygments`](a11y_pygments/) directory has the style of each theme, a description file in Markdown and the source CSS file.

For example:

```text
├── a11y_pygments
│   ├── a11y_dark
│   │   ├── __init.py__
│   │   ├── style.py     # pygments style defintion
│   │   ├── style.css    # rendered css file from the pygments definition
│   │   ├── README.md    # theme description in markdown
│   ├── a11y_light
│   │   ├── style.py
│   │   ├── style.css
│   │   ├── README.md
```

To add a new theme, create a folder with your new theme name, like `white-cats` and add the three files described before (so that it matches the rest of the themes).
You can copy the [`templates/new-theme`](templates/new-theme/) directory as a starting point ✨.

### 2. Customize your `style.py` file

We recommend you use the files in the [`templates/new-theme`](templates/new-theme/) as a starting point.

> **NOTE** 📝
> Please try to encapsulate all the raw colors in the `Colors` `enum` and call them in the rules section.
> This will help us with maintenance 🙏.

### 3. Visualize and debug your theme

While working on your theme, it might be helpful to generate individual HTML files to check the syntax highlighting for various programming languages.

To do so you can use the following command:

```bash
hatch dev:render_html
```

If successful, you should be able to see the results of your new theme under `test/html-files/<your-theme>`.

### 4. Update the `README.md` file for your theme

Once you are happy with the colors and the rules in the style file, update the README for your new theme!

The **most** important part for us, is to add a table with the contrast ratios of the colors you've chosen and their compliance to WCAG. Please use any of the current themes as a base, and use any color contrast checker to fill it out.

Some free contrast checking tools you can use are:

- [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/)
- [Adobe Color accessibility tools](https://color.adobe.com/create/color-contrast-analyzer)

Please add any acknowledgements to any themes you used for inspiration to the main [README](./README.md) in the repo under the `Acknowledgements` section.

Also, don't forget to add the name of your theme to our list of supported themes in the main [README](./README.md) as well as the appropriate classification (AA/AAA conformant).

### 5. Generate the source `style.css` file

You can generate your theme's CSS source file with the following command:

```bash
hatch dev:create_css
```

This will add the CSS file under `a11y_pygments/<your-theme>/style.css` and in the `docs` directory (which is used for our online demo).

### 6. Add your theme to our static page

We have a demo page where we showcase all the themes and the highlighting for a number of programming languages.

To add your new theme to the demo page:

1. Open the [docs/index.html](docs/index.html) file in the repo.
2. Add a new link to your new theme in the `themes` section:

   ```HTML
   ...
   <!-- themes -->
   <link rel="stylesheet" type="text/css" title="a11y dark" href="./../a11y_pygments/a11y_dark/style.css">
   <link rel="stylesheet" type="text/css" title="YOUR THEME HERE" href="./../a11y_pygments/<your-theme>/style.css">
   ...

   ```

With this change you should be able to open the `docs/index.html` file in your favorite browser and find your new theme in our demo!

You can also use Python `http.server` to view the demo page on `[http://localhost:8000/](http://localhost:8000/)` in your web browser.

```bash
python -m http.server --directory docs/
```

### 7. Create a Pull Request

Once you have added and verified your theme you should be ready to open a Pull Request 👏🏻
