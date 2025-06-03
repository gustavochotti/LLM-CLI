# llm/logger.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

def log_error(message: str):
    logging.error(message)

def log_info(message: str):
    logging.info(message)