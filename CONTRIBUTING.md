# Contributing to accessible pygments themes

Welcome! And thanks for taking your time to contribute to this project 🤩

## Submit an issue 📬

Please share your thoughts for fixes and features in the issue tracker. Add a clear description and please provide useful environment information.

## Creating your development environment 👩🏻‍💻 👨🏼‍💻

For creating your development environment locally please be sure to have the following tools installed,

- 🐍 An environment manager like `conda` or `pyenv`
- 📝 `git`

### Fork this repository ⏬

Fork this repository to your profile and clone it,

```
git clone <LINK-TO-YOUR-FORK>
```

Remember that this fork is a copy of the repository and any change done in it doesn't damage the original one.

### Install dependencies 💽

Once you have the local clone in your machine, we need to install the dependencies. For it, first we will create a new environment,

```
conda create -n a11y-pygments-dev python=3.9
conda activate a11y-pygments-dev
pip install -e .
```

After running this instructions you will have an environment named `a11y-pygments-dev`, with the requirements installed and this package installed in development version.

### Run the tests 🏃🏻‍♀️ 🏃‍♂️

Once the development environment is ready just run,

```
python test/run_tests.py
```

You will see the results under `test/results` in html format for each supported theme. We recommend to use your favorite browser to visualize fully visualize the result.


## Adding a new theme 🎨

### Where to put my new theme 👩🏼‍🎨

Our package is divided by themes, where each folder has the style of each theme, a description in markdown and the source css file.

```
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

For adding a new theme, please create a folder with your new theme name, like `white-cats` and add the three files described before.

### Fill `style.py` file

You can use as a base one of our existing themes, this file needs to define a new class with the new colors and rules you want.

---
📝 **NOTE** 📝

Please try to encapsulate all the raw colors in the `Colors` enum and call them in the rules section. This will help us with maintenance 🙏.

---

In order to see and debug your theme please add an entrypoint to it in the `setup.py` file found in the root of this repo,

```
...

  entry_points ={
    "pygments.styles": [
        "a11y-light = a11y_pygments.a11y_light.style:A11yLightStyle",
        "a11y-dark = a11y_pygments.a11y_dark.style:A11yDarkStyle",
        "my-theme = a11y_pygments.my_theme.style:MyTheme",
        ]
  },

...
```

Then, you will be able to add it to the list of themes in `run_tests.py` file,

```
...

themes = [
    "a11y-light",
    "a11y-dark",
    "my-theme"
    ]

...
```

Afterwards, you will be able to run the tests and see the results of your new theme under `test/results` in html format.

### Fill `README.md` file

Once you are happy with the colors and the rules in the style file, please fill out the readme for your new theme!

The **most** important part for us, is to add a table with the contrast ratios of the colors you've chosen and their compliance to WCAG. Please use any of the current themes as a base, and use any color contrast checker to fill it out.

Any acknowledgements to other repositories that you may used as base please add them as well to the main readme in the repo under the `acknowledgements` section.

### Generate source `style.css` file

We have an automatic way to generate this file by,

```
python a11y_pygments/utils/generate_css.py
```

The file should appear in the folder of your new theme.

### Create a Pull Request

Once you have the folder with the described files, please open a Pull Request 👏🏻
