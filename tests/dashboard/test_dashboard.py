import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(
            self,
            dashboard_page_with_state: DashboardPage
    ):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.toolbar_view.check_visible()
