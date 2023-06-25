import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        name_file = []
        for path in path_to_file:
            split_path_file = path.split('\\')
            name_file.append(split_path_file[-1])
            print(path.split('\\'))

        url_for_response = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        file_num = 0
        for file in path_to_file:
            params = {
                'path': name_file[file_num]
            }
            headers = {
                'Authorization': token
            }
            response_get_url = requests.get(url_for_response, params=params, headers=headers)
            print(response_get_url)
            url_for_upload = response_get_url.json().get('href', '')
            with open(file, 'rb') as file_upload:
                response_upload = requests.put(url_for_upload, files={'file': file_upload})
                print(response_upload)
            file_num += 1
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ....
    token = ....
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
