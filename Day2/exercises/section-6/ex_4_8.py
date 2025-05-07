import logging

def setup_logger(debug=False):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

def log_based_on_flag(logger, debug):
    if debug:
        logger.debug("This is a debug message, shown only if debug=True")
    logger.info("This is an info message, always shown.")

logger = setup_logger(debug=True)
log_based_on_flag(logger, debug=True)
