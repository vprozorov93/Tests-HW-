import pytest
from ya_api import YaUploader, token

@pytest.fixture
def data():
    return 'TestFolder13'


class TestFunction:
    def setup(self):
        self.YaUploader = YaUploader(token)
        
    def test_create_folder(self, data):
        yad = self.YaUploader
        assert yad.create_folder(data) == 201
        assert yad.get_folder_info(data) == 200

    def test_erorr_create_folder(self, data):
        yad = self.YaUploader
        assert yad.create_folder(data) == 201

    def test_error_check_folder(self, data):
        yad = self.YaUploader
        assert yad.get_folder_info(data+'1') == 200
