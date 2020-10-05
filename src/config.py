from os import getenv, urandom


class Config:
    CHARSET = getenv('ENCODING', getenv('CHARSET', 'utf-8'))
    DEBUG = getenv('FLASK_DEBUG', False)
    HOST = getenv('FLASK_RUN_HOST', '127.0.0.1')
    LANG = getenv('LANGUAGE', getenv('LANG', 'en'))
    PORT = getenv('FLASK_RUN_PORT', 5000)
    PROTOCOL = 'https' if getenv('FLASK_RUN_CERT', None) and getenv('FLASK_RUN_KEY', None) else 'http'


class MixinConfig(Config):
    SECRET_KEY = urandom(16)


class StageConfig(MixinConfig):
    True


class TestingConfig(MixinConfig):
    TESTING = True
