import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

def process_data(logger, data):
    logger.info(f"Processing data: {data}")

# Example usage
logger = setup_logger()
data = [1, 2, 3, 4, 5]
process_data(logger, data)
