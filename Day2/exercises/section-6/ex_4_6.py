import logging

def setup_file_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="app.log", filemode="w")
    logger = logging.getLogger(__name__)
    return logger

def log_to_file(logger, message):
    logger.info(message)

logger = setup_file_logger()
log_to_file(logger, "This is logged to a file.")
