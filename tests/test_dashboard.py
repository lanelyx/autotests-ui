import pytest

from pages.dashboard_page import DashboardPage
from components.navigation.sidebar_component import SidebarComponent


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(
        dashboard_page_with_state: DashboardPage
):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.sidebar.check_visible()

    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.toolbar_view.check_visible()
