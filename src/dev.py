
if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from config import StageConfig
    from util import route
    from util.commands import commands

else:
    from .config import StageConfig
    from .util import route
    from .util.commands import commands

app = route(config=StageConfig, name=__name__)
commands(app=app)
