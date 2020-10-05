
from os import getenv, sep
from flask import send_from_directory


def routes(app):

    @app.route(rule='/')
    def hello_world():
        return 'Hello World!'

    app.config['UPLOAD_FOLDER'] = getenv('HOME') + sep + 'Downloads'

    @app.route(rule='/jpg/<path:filename>')
    def jpg_render(filename):
        return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename, mimetype='image/jpeg')

