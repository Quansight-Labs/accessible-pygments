import os

from a11y_pygments.utils.utils import generate_css, get_themes_names

act_folder = os.path.dirname(__file__)
themes = get_themes_names()
generate_css(themes, save_dir=act_folder)
