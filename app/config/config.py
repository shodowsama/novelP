# 全局配置
class Config(object):
    db_url = 'mysql+pymysql://root:820713@127.0.0.1:3306/novels'

# 開發環境配置
class DevelopmentConfig(Config):
    log_level = 'DEBUG'

# 生產環境配置
class ProductionConfig(Config):
    log_level = 'INFO'



config={
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    }