from utils.error_handler import ErrorHandler

def test_handle_api_error():

    assert ErrorHandler.handle_api_error(404) == "Resource not found."
    assert ErrorHandler.handle_api_error(500) == "Server error. Please try again later."
    assert ErrorHandler.handle_api_error(123) == "An unexpected error occurred."

def test_log_error(tmp_path):
 
    log_file = tmp_path / "error_log.txt"
    
 
    ErrorHandler.log_error("Test Error", str(log_file))

    assert log_file.exists()
    
    with open(log_file, "r") as file:
        content = file.read()
    assert "Test Error" in content
