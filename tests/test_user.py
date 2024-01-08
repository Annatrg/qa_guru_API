from helpers.base_api import BaseApi

base_api = BaseApi()


def test_add_item_in_basket(api_url, headers):
    item = base_api.get_item(api_url=api_url)
    base_api.add_item_in_basket(api_url=api_url, item=item, headers=headers)


def test_delete_item_in_basket(api_url, headers):
    item = base_api.get_item(api_url=api_url)
    base_api.add_item_in_basket(api_url=api_url, item=item, headers=headers)
    base_api.delete_item_in_basket(api_url=api_url, headers=headers)
