import logging

def setup_logger():
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

def log_error_with_code(error_code, message):
    logger = setup_logger()
    logger.error(f"Error {error_code}: {message}")

log_error_with_code(404, "Resource not found.")
