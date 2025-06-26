import logging
from logging.handlers import RotatingFileHandler
from app.config.config import config
from app.setting import env

# 日誌配置
def setup_logging():
    # 日誌等級
    logging.basicConfig( level = config[env].log_level )
    # 創建日誌紀錄器(路徑，最大大小，保留的備份數量)
    file_log_handler = RotatingFileHandler('log/novels.log', maxBytes=1024*1024*10, backupCount=5)
    # 日誌格式
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(filename)s : %(lineno)d __ %(message)s")
    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)


setup_logging()