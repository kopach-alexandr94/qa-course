import requests
import pytest

@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )
def test_func():
    requests.get('http://ya.ru')








