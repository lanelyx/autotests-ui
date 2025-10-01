from playwright.sync_api import sync_playwright, expect
import pytest


def check_visible_and_text(locator, text):
    """
    Не уверен, что правильно понял слова про "Проверяется наличие и текст",
    но на всякий случай добавил проверку на видимость, для проверки,
    что вообще пользователю видны эти элементы, наличие как я понял отдельно
    проверять не нужно, тк при PLaywright при обращении уже проверяет его наличие в DOM
    """
    expect(locator).to_be_visible()
    expect(locator).to_have_text(text)


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser_state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser_state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        check_visible_and_text(header_courses, 'Courses')

        no_result_header = page.get_by_test_id('courses-list-empty-view-title-text')
        check_visible_and_text(no_result_header, 'There is no results')

        icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()  # кажется покрывает требование по наличию и видимости элемента

        paragraph_with_explanation = page.get_by_test_id('courses-list-empty-view-description-text')
        check_visible_and_text(paragraph_with_explanation,
                               'Results from the load test pipeline will be displayed here')
