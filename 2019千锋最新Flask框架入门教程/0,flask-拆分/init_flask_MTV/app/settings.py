class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class TestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class StagingConfig(Config):  # ÑÝÊ¾»·¾³
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class ProductConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
