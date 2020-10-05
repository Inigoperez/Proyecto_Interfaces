
if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from config import MixinConfig
    from util import route

else:
    from .config import MixinConfig
    from .util import route

route(config=MixinConfig, name=__name__)
