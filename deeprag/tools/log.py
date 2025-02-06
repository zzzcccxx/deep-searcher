import logging

# config log
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def set_level(level):
    """set log level"""
    logging.getLogger().setLevel(level)


def debug(message):
    """debug log"""
    logging.debug(message)


def info(message):
    """info log"""
    logging.info(message)


def warning(message):
    """warning log"""
    logging.warning(message)


def error(message):
    """error log"""
    logging.error(message)


def critical(message):
    """critical log"""
    logging.critical(message)
