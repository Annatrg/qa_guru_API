import jsonschema
import requests
import allure
import json


class BaseApi:

    def get_item(self, api_url):
        method = 'GET'
        endpoint = '/rg/v1/newRG/products/search?fields=FULL&pageSize=24&categoryCode=Perfumery'
        with allure.step('Получить список доступных товаров для заказа'):
            response = requests.request(method=method, url=f'{api_url}{endpoint}')
        with allure.step('Убедиться, что на метод /products/search получен статус 200'):
            assert response.status_code == 200, f'Статус код не 200. Получен статус код {response.status_code}'
        # нет проверки на схему, так как схема получается на 4237 строк
        with allure.step('Получить код первого товара'):
            item = response.json()['results'][0]['code']
            if len(item) == 6 or len(item) == 7:
                pass
            else:
                item = item[5:12]
        print(item)
        return item

    def add_item_in_basket(self, api_url: str, item: str, headers, quantity: str = '1'):
        method = 'POST'
        endpoint = '/rg/v1/newRG/carts/current/entries'
        query_params = f'qty={quantity}&code={item}'
        with allure.step('Добавить товар в корзину'):
            response = requests.request(method=method, url=f'{api_url}{endpoint}?{query_params}', headers=headers)
        with allure.step('Убедиться, что на метод /carts/current/entries получен статус 200'):
            assert response.status_code == 200, f'Статус код не 200. Получен статус код {response.status_code}'
        with allure.step('Убедиться, что схема ответа соответствует ожидаемой'):
            with open('C:/Users/annaa/PycharmProjects/qa_guru_API/helpers/json_schema/add_item_in_basket.json') as file:
                schema = json.load(file)
                jsonschema.validate(response.json(), schema), f'Схема ответа не соответствует ожидаемой'
        return response

    def delete_item_in_basket(self, api_url: str, headers):
        method = 'DELETE'
        endpoint = '/rg/v1/newRG/carts/current/entries/0'
        with allure.step('Удалить товар из корзины'):
            response = requests.request(method=method, url=f'{api_url}{endpoint}', headers=headers)
        with allure.step('Убедиться, что на метод /carts/current/entries/0 получен статус 200'):
            assert response.status_code == 200, f'Статус код не 200. Получен статус код {response.status_code}'
        with allure.step('Убедиться, что схема ответа соответствует ожидаемой'):
            with open('C:/Users/annaa/PycharmProjects/qa_guru_API/helpers/delete_item_in_basket.json') as file:
                schema = json.load(file)
                jsonschema.validate(response.json(), schema), f'Схема ответа не соответствует ожидаемой'
        return response
