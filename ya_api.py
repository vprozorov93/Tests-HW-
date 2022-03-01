import requests

token = 'AQAAAAAZR95QAADLWyk3oq-Md0PZpQKmkPRRi5Y'


class YaUploader:
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        """
        Инициализируем объект класса с токеном для API
        :param token:
        """
        self.token = token

    def get_headers(self):
        """
        Метод для получения статичных headers под запросы
        :return: Возвращает headers для выполнения запросов
        """
        return {'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        """
        Получаем список файлов на ЯндексДиске
        :return: Возвращает список файлов в json формате
        """
        files_url = f'{self.url}v1/disk/resources/files'
        headers = self.get_headers()

        response = requests.get(url=files_url, headers=headers)
        return response.json()

    def create_folder(self, path: str):
        files_url = f'{self.url}v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(url=files_url, headers=headers, params=params)
        return response.status_code

    def get_folder_info(self, path: str):
        files_url = f'{self.url}v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.get(url=files_url, headers=headers, params=params)
        return response.status_code
