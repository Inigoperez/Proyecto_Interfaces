
from click import echo


def commands(app):

    @app.cli.command(short_help='Map the routes, the endpoints with its methods and its rules')
    def router():
        return echo(app.url_map)
