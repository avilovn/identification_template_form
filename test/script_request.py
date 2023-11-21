import requests


def send_to_backend_request_examples():
    url = 'http://localhost:8000/v1/templates/get_form'

    request_1 = {
        'field_name_1': 'nikita-maklakov97@yandex.ru',
    }

    request_2 = {
        'field_name_1': 'nikita-maklakov97@yandex.ru',
        'field_name_2': '20.02.2022',
        'field_name_3': '+7 999 999 99 99',
        'field_name_4': 'Text'
    }

    request_3 = {
        'field_name_4': 'Text',
        'field_name_5': 'nikita-maklakov97@yandex.ru'
    }
    try:
        response_1 = requests.post(url, data=request_1)
        response_2 = requests.post(url, data=request_2)
        response_3 = requests.post(url, data=request_3)
        print(f"Пример №1. Входные данные:\n{request_1}")
        print(f"Пример №1. Выходные данные:\n{response_1.text}")
        print(f"Пример №2. Входные данные:\n{request_2}")
        print(f"Пример №2. Выходные данные:\n{response_2.text}")
        print(f"Пример №3. Входные данные:\n{request_3}")
        print(f"Пример №3. Выходные данные:\n{response_3.text}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    send_to_backend_request_examples()
