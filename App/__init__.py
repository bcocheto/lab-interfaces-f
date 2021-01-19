from flask import Flask, render_template
import os

app = Flask(
    __name__,
    static_folder=os.path.abspath("App/view/static"),
    template_folder=os.path.abspath("App/view/templates"),
)

from App.controller.index_controller import index
