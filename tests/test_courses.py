from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
        create_courses_page: CreateCoursePage,
        courses_list_page: CoursesListPage
):
    create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_courses_page.check_visible_create_course_title()
    create_courses_page.check_disabled_create_course_button()
    create_courses_page.check_visible_image_preview_empty_view()
    create_courses_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_courses_page.check_visible_create_course_form(
        title='',
        description='',
        estimated_time='',
        max_score='0',
        min_score='0'
    )
    create_courses_page.check_visible_create_exercises_title()
    create_courses_page.check_visible_create_exercises_button()
    create_courses_page.check_visible_exercises_empty_view()
    create_courses_page.upload_preview_image(file="./testdata/files/image.png")
    create_courses_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_courses_page.fill_create_course_form(
        title='Playwright',
        estimated_time='2 weeks',
        description='Playwright',
        max_score='100',
        min_score='10'
    )
    create_courses_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title='Playwright',
        max_score='100',
        min_score='10',
        estimated_time='2 weeks'
    )
