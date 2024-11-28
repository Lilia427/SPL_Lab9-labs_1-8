from user_interface.input_handler import InputHandler

def test_validate_email():
    assert InputHandler.validate_email("test@example.com")
    assert not InputHandler.validate_email("invalid-email")

def test_validate_date():
    assert InputHandler.validate_date("2024-01-01")
    assert InputHandler.validate_date("01/01/2024")
    assert not InputHandler.validate_date("invalid-date")

def test_validate_phone():
    assert InputHandler.validate_phone("+1234567890")
    assert not InputHandler.validate_phone("12345")
