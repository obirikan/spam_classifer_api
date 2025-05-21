import logging

# Logger setup
logger = logging.getLogger("spam_detector")
logger.setLevel(logging.DEBUG)

# Handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Handler levels
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# duplicate handler 
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def log(text: str, level: str = "info", exc_info: bool = False) -> None:
    """
    Log messages at different levels
    
    Args:
        text: The message to log
        level: The logging level (debug, info, warning, error, critical)
        exc_info: Whether to include exception information
    """
    if level == "debug":
        logger.debug(text, exc_info=exc_info)
    elif level == "info":
        logger.info(text, exc_info=exc_info)
    elif level == "warning":
        logger.warning(text, exc_info=exc_info)
    elif level == "error":
        logger.error(text, exc_info=exc_info)
    elif level == "critical":
        logger.critical(text, exc_info=exc_info)
    else:
        logger.info(text)
