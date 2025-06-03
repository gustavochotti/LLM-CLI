from logger import log_error

def handle_exception(e: Exception, context: str = ""):
    msg = f"{context}: {e}" if context else str(e)
    log_error(msg)