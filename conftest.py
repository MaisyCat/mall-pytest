import time

import pytest

@pytest.fixture(scope="session")
def username():
    return "member"

@pytest.fixture(scope="session")
def password():
    return "member123"

@pytest.fixture(scope="session")
def operator_with_auth(username, password):
    """
    登录操作
    :return:
    """
    print("登录后的操作")
    from common.request_util import RequestUtil
    client = RequestUtil("http://localhost:8201/mall-portal")
    client.login(username,password)
    yield client
    print("结束")
    client.close()


@pytest.fixture(scope="function")
def operator_without_auth():
    """
    不登录操作
    比如说设计登录的测试用例啊，不进行保存token操作和携带
    :return:
    """
    from common.request_util import RequestUtil
    client = RequestUtil("http://localhost:8201/mall-portal")
    yield client
    client.close()