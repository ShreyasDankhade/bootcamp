import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

def log_info(logger, message):
    logger.info(message)

logger = setup_logger()
log_info(logger, "This is an informational message.")
