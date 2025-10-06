from playwright.sync_api import Page, Route


# def abort(route: Route):   # без лямбда
#     print(f"\nAborting url: {route.request.url}")
#     route.abort()


def mock_state_resourses(page: Page):
    page.route("**/*.{ico,png,jpg,svg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort()) # с лямбда