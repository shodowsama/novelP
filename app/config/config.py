# 全局配置
class Config(object):
    db_url = ''

# 開發環境配置
class DevelopmentConfig(Config):
    db_url = 'mysql+pymysql://root:820713@127.0.0.1:3306/novels'

# 生產環境配置
class ProductionConfig(Config):
    db_url = ''



config={
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    }