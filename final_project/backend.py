from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
import visiualization

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

app = Flask(__name__, static_folder="templates")

@app.route("/")
def index():
    #c = visiualization.show_olympic_athete("summer")
    c = visiualization.show_sports(year=1896, sports="Athletics")
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run()