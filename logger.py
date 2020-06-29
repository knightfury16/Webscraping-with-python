import logging
import os


class Logger:

    @classmethod
    def create_logger(cls, name, level, file_handler_name=os.environ.get("FILE_HANDLER_NAME") or "logger.log"):

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

        file_handler = logging.FileHandler(file_handler_name)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)

        stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(logging.DEBUG)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger
