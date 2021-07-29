from flask import Blueprint, render_template

blueprint = Blueprint('form_controller', __name__)

@blueprint.route('/form')
def form_index():
  return render_template('form.html');