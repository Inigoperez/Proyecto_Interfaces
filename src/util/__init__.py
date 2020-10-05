

def flask(config):
    from os import getenv
    from flask import Flask
    app = Flask(__name__,
                static_url_path=None,
                static_folder=getenv('STATIC_FOLDER', 'static'),
                static_host=None,
                host_matching=False,
                subdomain_matching=False,
                template_folder=getenv('TEMPLATE_FOLDER', 'templates'),
                instance_path=None,
                instance_relative_config=False,
                root_path=None)
    app.config.from_object(config)

    return app


def route(config, name=__name__):
    if name == '__main__':
        from os import getcwd, sep
        from sys import path as syspath, version
        # @see https://stackoverflow.com/a/56999264
        syspath.append('{}{}__pypackages__{}{}{}lib'.format(getcwd(), sep, sep, version[0:3], sep))
        app = flask(config=config)
        from util.routes import routes
        routes(app=app)
        from templates import UI
        UI().run(app=app)

    else:
        app = flask(config=config)
        from .routes import routes
        routes(app=app)

    return app


