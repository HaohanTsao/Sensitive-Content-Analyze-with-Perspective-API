import os


class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


def get_config():
    env = os.getenv("ENV", "dev")
    if env == "prod":
        return Config()
    elif env == "test":
        return TestingConfig()
    else:
        return DevelopmentConfig()
