from flask.blueprints import Blueprint
from flask import render_template
from controller import OperatorController

# create new blueprint for API
web = Blueprint(__name__, "blueprint", static_folder="static", url_prefix='/', template_folder='../templates')

@web.get('/')
def index():
    return render_template('index.html')
# routes for 


# routes for 

