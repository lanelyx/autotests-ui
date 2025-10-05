import pytest
from _pytest.fixtures import SubRequest


# 1, 2, 3, 4

@pytest.mark.parametrize('number', [1, 2, 3, -1, 4, 5])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
def test_multiplication_of_numbers(browser: str, os: str):
    assert len(browser + os) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running open_browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit cards', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'Running user_with_operations: {user}, {account}')

    def test_user_without_operations(self, user: str):
        print(f'Running user_without_operations: {user}')


users = {
    'User with money': '79000000000',
    'User with a lot of money': '79000000001',
    'User without money': '79000000002',
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...
