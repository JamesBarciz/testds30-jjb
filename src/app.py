from flask import Flask


def create_app():
  app = Flask(__name__)

  @app.route('/')
  def base():
    return 'This is the base route of my application.'

  return app
