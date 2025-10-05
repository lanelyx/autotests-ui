from playwright.sync_api import sync_playwright, Request, Response

from tools.routes import AppRoute


def log_request(request: Request): # функция принтит логи по настройкам в ней по реквесту
    print(f'Request: {request.method} {request.url}')


def log_response(response: Response): # функция принтит логи по настройкам в ней по респонсу
    print(f'Response: {response.status} {response.url}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    page.on('request', log_request) # включить "логирование"
    # page.remove_listener('request', log_request) # выключить "логирование"
    page.on('response', log_response) # включить "логирование"

    page.wait_for_timeout(5000)