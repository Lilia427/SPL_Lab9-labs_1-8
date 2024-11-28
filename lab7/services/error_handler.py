class ErrorHandler:
    @staticmethod
    def handle_api_error(response):
        status_code = response if isinstance(response, int) else response.status_code
        if status_code == 404:
            return "Resource not found."
        elif status_code == 500:
            return "Server error. Please try again later."
        else:
            return "An unexpected error occurred."

    @staticmethod
    def log_error(message, file_path="error_log.txt"):
        with open(file_path, "a") as file:
            file.write(f"Error: {message}\n")
