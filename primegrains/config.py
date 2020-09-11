import os
import re

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    WEBPACK_LOADER = {
        'BUNDLE_DIR_NAME': os.path.join('./static', 'dist'),
        'STATIC_URL': 'static',
        'STATS_FILE': os.path.join(APP_ROOT, 'app', 'static', 'dist', 'webpack-bundle.dev.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORES': [re.compile(r'.+\.hot-update.js'), re.compile(r'.+\.map')]
    }

    @staticmethod
    def init_app(app):
        print('THIS APP IS IN DEBUG MODE.')


class TestingConfig(Config):
    TESTING = True

    @staticmethod
    def init_app(app):
        print('THIS APP IS IN TESTING MODE.')


class ProductionConfig(Config):
    DEBUG = False

    WEBPACK_LOADER = {
        'BUNDLE_DIR_NAME': os.path.join('./static', 'dist'),
        'STATIC_URL': 'static',
        'STATS_FILE': os.path.join(APP_ROOT, 'app', 'static', 'dist', 'webpack-bundle.prod.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORES': [re.compile(r'.+\.hot-update.js'), re.compile(r'.+\.map')]
    }

    @staticmethod
    def init_app(app):
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
