import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

def log_user_action(user_id, action):
    logger = setup_logger()
    logger.info(f"User {user_id} performed action: {action}")

log_user_action(123, "login")
