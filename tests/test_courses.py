from playwright.sync_api import expect, Page
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
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    check_visible_and_text(header_courses, 'Courses')

    no_result_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    check_visible_and_text(no_result_header, 'There is no results')

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()  # кажется покрывает требование по наличию и видимости элемента

    paragraph_with_explanation = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    check_visible_and_text(paragraph_with_explanation,
                           'Results from the load test pipeline will be displayed here')
