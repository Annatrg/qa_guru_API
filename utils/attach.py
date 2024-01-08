import json
import allure

from allure_commons.types import AttachmentType


def request_body(request_body_json):
    allure.attach(
        name='Request body',
        body=request_body_json,
        attachment_type=allure.attachment_type.JSON,
        extension='json'
    )


def response_body(response_body_json):
    allure.attach(
        name='Response body',
        body=json.dumps(response_body_json),
        attachment_type=allure.attachment_type.JSON,
        extension='json'
    )


def response_code(response_status_code):
    allure.attach(
        name='Response status code',
        body=response_status_code,
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

