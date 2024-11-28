from user_interface.output_handler import OutputHandler

def test_display_message(capsys):
    OutputHandler.display_message("Test Message", color="\033[92m")
    captured = capsys.readouterr()
    assert "Test Message" in captured.out
