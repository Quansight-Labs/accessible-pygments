from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Top-level package directory
pkg_dir = Path(__file__).parent.parent
templates_dir = pkg_dir / "templates"
styles_dir = pkg_dir / "docs" / "css"

# index template
environment = Environment(loader=FileSystemLoader(templates_dir))
index_tpl = environment.get_template("index_template.html")
# output
rendered = pkg_dir / "docs" / "index.html"


styles = [style.name for style in styles_dir.iterdir()]


def get_names(styles):
    themes_meta = []
    for style in styles:
        title = Path(style).stem.split("-")[0].replace("_", " ")
        theme_meta = {"style": Path(style).name, "title": title}
        themes_meta.append(theme_meta)
    return themes_meta


def render_template(context) -> None:
    with open(rendered, mode="w", encoding="utf-8") as f:
        f.write(index_tpl.render(context))


if __name__ == "__main__":
    themes = get_names(styles)
    context = {"themes": themes}
    render_template(context=context)
