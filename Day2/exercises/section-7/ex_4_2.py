import time
import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)

def log_function_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger = setup_logger()
        logger.debug(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_function_performance
def slow_function():
    time.sleep(2)

# Example usage
slow_function()
