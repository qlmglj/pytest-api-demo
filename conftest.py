import pytest

from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api():
    """jsonplaceholder：Fake REST API。"""
    client = ApiClient("https://jsonplaceholder.typicode.com")
    yield client
    client.close()


@pytest.fixture(scope="session")
def httpbin():
    """httpbin：请求回显服务，用于校验参数透传。"""
    client = ApiClient("https://httpbin.org")
    yield client
    client.close()
