import logging
from termcolor import colored

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': 'cyan',      
        'INFO': 'green',      
        'WARNING': 'yellow',  
        'ERROR': 'red',       
        'CRITICAL': 'magenta'
    }

    def format(self, record):
        # all line in log will be colored
        log_message = super().format(record)
        return colored(log_message, self.COLORS.get(record.levelname, 'white'))

        # only log level will be colored
        # levelname_colored = colored(record.levelname, self.COLORS.get(record.levelname, 'white'))
        # record.levelname = levelname_colored 
        # return super().format(record)
        
        # only keywords will be colored
        # message = record.msg
        # for word, color in self.KEYWORDS.items():
        #     if word in message:
        #         message = message.replace(word, colored(word, color))
        # record.msg = message
        # return super().format(record)

# config log
formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
root_logger = logging.getLogger()
for handler in root_logger.handlers:
    if isinstance(handler, logging.StreamHandler):
        handler.setFormatter(formatter)

dev_mode = False

def set_dev_mode(mode):
    """set dev mode"""
    global dev_mode
    dev_mode = mode

def set_level(level):
    """set log level"""
    logging.getLogger().setLevel(level)


def debug(message):
    """debug log"""
    if dev_mode:
        logging.debug(message)


def info(message):
    """info log"""
    if dev_mode:
        logging.info(message)


def warning(message):
    """warning log"""
    if dev_mode:
        logging.warning(message)


def error(message):
    """error log"""
    if dev_mode:
        logging.error(message)


def critical(message):
    """critical log"""
    if dev_mode:
        logging.critical(message)

def color_print(message, **kwargs):
    logging.info(message)