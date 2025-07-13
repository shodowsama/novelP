
from app.app import create_app
import logging

app = create_app()


if __name__ == '__main__':
    logging.info("Starting the application...")
    logging.debug("DEBUG: 運行debug模式")

    app.run()