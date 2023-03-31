# Contributing to accessible pygments themes

Welcome! And thanks for taking your time to contribute to this project 🤩

- [Contributing to accessible pygments themes](#contributing-to-accessible-pygments-themes)
  - [Submit an issue 📬](#submit-an-issue-)
  - [Contributing to this package](#contributing-to-this-package)
    - [Prerequisites 📦](#prerequisites-)
    - [Creating your development environment 👩🏻‍💻 👨🏼‍💻](#creating-your-development-environment--)
    - [Run the tests 🏃🏻‍♀️ 🏃‍♂️](#run-the-tests-️-️)
  - [Adding a new theme 🎨](#adding-a-new-theme-)
    - [Where to add a new theme 👩🏼‍🎨](#where-to-add-a-new-theme-)
    - [Customize your `style.py` file](#customize-your-stylepy-file)
    - [Visualize and debug your theme](#visualize-and-debug-your-theme)
    - [Update the `README.md` file](#update-the-readmemd-file)
    - [Generate source `style.css` file](#generate-source-stylecss-file)
      - [Add your theme to our static page](#add-your-theme-to-our-static-page)
    - [Create a Pull Request](#create-a-pull-request)

## Submit an issue 📬

Please share your thoughts for fixes and features in the issue tracker.
When doing so, please a clear description and provide useful environment information.
Please share your thoughts for fixes and features in the issue tracker. Add a clear description, and please provide useful environment information.

## Contributing to this package

For creating your development environment locally you will need to have the following tools installed:

### Prerequisites 📦

You will need to have the following installed locally:

- `git`
- Python >= 3.9
- [hatch](https://hatch.pypa.io/)

### Creating your development environment 👩🏻‍💻 👨🏼‍💻

1. Fork this repository to your GitHub account, then clone it to your local machine:

   ```bash
    git clone <LINK-TO-YOUR-FORK>
   ```

   Remember that this fork is a copy of the repository and any change done in it doesn't affect the original one.

2. From here you can create your local environments with hatch:

   ```bash
       hatch env create
   ```

3. You can verify that the environment was created successfully by running:

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

### Run the tests 🏃🏻‍♀️ 🏃‍♂️

Once the development environment is ready run the following command:

```bash
python test/run_tests.py
```

You will see the results under `test/results` in HTML format for each supported theme.
We recommend using your favorite browser to see the rich HTML output.

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

To add a new theme, please create a folder with your new theme name, like `white-cats` and add the three files described before (so that it matches the rest of the themes).

### Customize your `style.py` file

You can use as a base one of our existing themes, this file needs to define a new class named `Theme` with the new colors and rules you want.

> **NOTE** 📝
> Please try to encapsulate all the raw colors in the `Colors` `enum` and call them in the rules section.
> This will help us with maintenance 🙏.

### Visualize and debug your theme

To see and debug your theme re-install the package via:

```bash
pip install -e .
```

Then generate the HTML results:

```bash
python test/run_tests.py
```

If successful, you should be able to see the results of your new theme under `test/results/<your-theme>` in HTML format.

### Update the `README.md` file

Once you are happy with the colors and the rules in the style file, please update the README for your new theme!

The **most** important part for us, is to add a table with the contrast ratios of the colors you've chosen and their compliance to WCAG. Please use any of the current themes as a base, and use any color contrast checker to fill it out.

Any acknowledgements to other repositories that you may use as base please add them as well to the main [README](./README.md) in the repo under the `acknowledgements` section.

Also, don't forget to add the name of your theme to our list of supported themes in the main README.

### Generate source `style.css` file

You can generate the CSS file automatically through:

```bash
python a11y_pygments/test/run_css.py
```

The file should appear in the folder of your new theme.

#### Add your theme to our static page

We have a demo page where you will be able to change the style of different languages at the same time.
To add your new theme please go to the file `test/index.html`. Under themes, we have a link to all the generated CSS files.

You will have to manually add a new link to your new theme:

```HTML
...
<!-- themes -->
<link rel="stylesheet" type="text/css" title="a11y dark" href="./../a11y_pygments/a11y_dark/style.css">
<link rel="stylesheet" type="text/css" title="YOUR THEME HERE" href="./../a11y_pygments/<your-theme>/style.css">
...

```

With this change you will be able to open `test/index.html` in your favorite browser and find your new theme in our demo!

### Create a Pull Request

Once you have the folder with the described files, please open a Pull Request 👏🏻
