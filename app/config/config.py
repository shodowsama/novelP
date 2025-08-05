# 全局配置
class Config(object):
    db_url = 'mysql+pymysql://root:820713@127.0.0.1:3306/novels'
    # 顯示條數
    page_count = 10

    book_status_map= {'1':'不限','2':'连载','3':'全本'}
    book_type_map= {'1':'全部', '2':'官场职场', '3':'玄幻魔法',
                    '4':'都市小说', '5':'修真武侠', '6':'言情小说', '7':'科幻空间'}


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