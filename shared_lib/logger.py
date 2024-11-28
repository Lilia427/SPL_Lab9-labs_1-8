import logging

class Logger:
    """A class for logging events in the project."""

    def __init__(self, log_file="application.log"):
        """Initialize the logger with a specified log file."""
        self.logger = logging.getLogger("SharedLogger")
        self.logger.setLevel(logging.DEBUG)
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Adding handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Log an informational message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical error message."""
        self.logger.critical(message)
