import os
from a11y_pygments.utils.utils import find_all_themes, generate_css


act_folder = os.path.dirname(__file__)
themes = find_all_themes()
generate_css(themes, save_dir=act_folder)
