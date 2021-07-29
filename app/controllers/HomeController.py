from flask import Blueprint, render_template

blueprint = Blueprint('home_controller', __name__)

@blueprint.route('/')
def home():
  return render_template('index.html', name='Flask App')