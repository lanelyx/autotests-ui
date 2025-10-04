from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
