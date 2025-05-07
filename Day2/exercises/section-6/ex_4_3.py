import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

def log_user_info(logger, user):
    logger.debug(f"User: {user['name']}, Age: {user['age']}")

# Example usage
logger = setup_logger()
user = {"name": "Shreyas", "age": 30}
log_user_info(logger, user)