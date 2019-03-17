import logging
import inspect


def custom_logger(log_level=logging.DEBUG):
    """Custom logger class"""

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    logger.setLevel(level=logging.DEBUG)

    file_handler = logging.FileHandler('automation.log', mode='w')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%Y%m%dT%H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
