import logging
import os

def setup_logger():
    debug_mode = os.getenv("DEBUG", "False") == "True"
    logging.basicConfig(level=logging.DEBUG if debug_mode else logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

# Example usage
logger = setup_logger()
logger.debug("This is a debug message.")
logger.info("This is an info message.")
