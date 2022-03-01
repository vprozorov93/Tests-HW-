import pytest
from ya_api import YaUploader, token

@pytest.fixture
def data():
    foo = YaUploader(token)
    return foo, 'TestFolder13'


class TestFunction:
    def test_create_folder(self, data):
        assert data[0].create_folder(data[1]) == 201
        assert data[0].get_folder_info(data[1]) == 200

    def test_erorr_create_folder(self, data):
        assert data[0].create_folder(data[1]) == 201

    def test_error_check_folder(self, data):
        assert data[0].get_folder_info(data[1]+'1') == 200
