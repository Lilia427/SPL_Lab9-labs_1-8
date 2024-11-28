# Configuration file for the project

# Base URL for the API
API_BASE_URL = "https://jsonplaceholder.typicode.com"

# File paths for saving data
HISTORY_FILE_PATH = "history/user_history.json"
ERROR_LOG_PATH = "error_log.txt"

# Default file names for exports
JSON_EXPORT_FILE = "exported_data.json"
CSV_EXPORT_FILE = "exported_data.csv"
TXT_EXPORT_FILE = "exported_data.txt"

# Console output configurations
TABLE_TITLE_COLOR = "\033[92m"  # Green color for table titles
TABLE_MESSAGE_COLOR = "\033[94m"  # Blue color for messages
TABLE_RESET_COLOR = "\033[0m"  # Reset to default

# API-specific configurations
MAX_POSTS_TO_DISPLAY = 5  # Maximum number of posts displayed at once
DEFAULT_USER_ID = 1  # Default user ID for API requests

# Debug mode (True to enable detailed logging)
DEBUG = True

# Default colors for dynamic settings
DEFAULT_TITLE_COLOR = "\033[92m"  # Green
DEFAULT_MESSAGE_COLOR = "\033[94m"  # Blue
