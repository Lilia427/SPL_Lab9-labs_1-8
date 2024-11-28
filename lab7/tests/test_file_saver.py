import os
from utils.file_saver import FileSaver

def test_save_to_json():
    data = [{"id": 1, "name": "Test"}]
    FileSaver.save_to_json(data, "test.json")
    assert os.path.exists("test.json")
    os.remove("test.json")

def test_save_to_csv():
    data = [{"id": 1, "name": "Test"}]
    FileSaver.save_to_csv(data, "test.csv", headers=["id", "name"])
    assert os.path.exists("test.csv")
    os.remove("test.csv")

def test_save_to_txt():
    data = "Test Data"
    FileSaver.save_to_txt(data, "test.txt")
    assert os.path.exists("test.txt")
    os.remove("test.txt")
