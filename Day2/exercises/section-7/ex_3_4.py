import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

def log_function_entry_and_exit(func):
    def wrapper(*args, **kwargs):
        logger = setup_logger()
        logger.debug(f"Entering {func.__name__}")
        result = func(*args, **kwargs)
        logger.debug(f"Exiting {func.__name__}")
        return result
    return wrapper

@log_function_entry_and_exit
def calculate_square(number):
    return number * number

result = calculate_square(5)