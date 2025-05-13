import logging.config
import os

from app import create_app
from modules.constants import LOGGING_CONFIG_FILE

if __name__ == '__main__':
    logging.config.fileConfig(LOGGING_CONFIG_FILE)

    logging.info('Запуск приложения')

    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
