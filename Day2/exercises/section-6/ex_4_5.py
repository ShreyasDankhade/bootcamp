import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

def log_error(logger, message):
    logger.error(message)

# Example usage
logger = setup_logger()
log_error(logger, "An error occurred while processing data.")
