class BaseConfig:
    RER_PAGE = 10
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = True