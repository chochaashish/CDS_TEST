import logging
from config import LOGGER_FILE_PATH


class Logger:

    def __init__(self):
        logging.basicConfig(filename=LOGGER_FILE_PATH,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

    def write_logs(self, message):
        logging.info(message)
