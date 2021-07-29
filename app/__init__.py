import os
from flask import Flask
from app.controllers import HomeController, FormController

def create_app():
  path = os.path.dirname(os.path.abspath(__file__))

  app = Flask(__name__)
  app.static_folder = path + '/views/static'
  app.template_folder = path + '/views/templates'

    # List Blueprints
  blueprints = [
    HomeController.blueprint,
    FormController.blueprint
  ]

  for bp in blueprints:
    app.register_blueprint(bp)
    
  return app

