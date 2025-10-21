import logging
from pathlib import Path
from datetime import datetime
import os

# if exists, returns LOG_LEVEL, else returns INFO
LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# formats
LOG_FORMAT = "[%(asctime)s] %(levelname)s %(name)s:%(lineno)d - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def setup_logging(log_to_file: bool=False):
    '''
    setup logging with handlers for console (always) and file (optional)

    Args:
        log_to_file: if True, saves logs in file
    '''

    # create a logger object
    root_logger = logging.getLogger()

    # clean past handlers
    root_logger.handlers.clear()

    # set level
    root_logger.setLevel(LEVEL)

    # apply format
    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)

    # console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(LEVEL)
    root_logger.addHandler(console)

    # file handler
    if log_to_file:

        # save root path
        ROOT = Path(__file__).resolve().parents[1]

        # where to save logs
        LOG_DIR = ROOT / "logs"

        # creates directory if doesnt exists
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        # log file name and path
        LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

        # file handler
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(LEVEL)
        root_logger.addHandler(file_handler)
    
    return root_logger

# logging test
if __name__ == '__main__':
    setup_logging(True)
    logging.info('Logging test: file & console')