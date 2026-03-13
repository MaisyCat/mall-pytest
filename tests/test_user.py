import pytest

from api.user_api import UserApi
from common.yaml_util import ddt


class TestUser:
    loginEndpoint="/sso/login"

    @pytest.mark.order(1)
    @ddt("data_login.yaml")
    def test_user_login(self,operator_without_auth,data):
        client=UserApi(operator_without_auth)
        res=client.login(self.loginEndpoint, data["username"], data["password"])
        assert res.status_code==data["expected"]["status"],"与预计状态码不一致"
        if res.status_code==200:
            res=res.json()
            assert res["code"]==data["expected"]["code"],"与预计code不一致"
            assert res["message"]==data["expected"]["message"],"与预计message不一致"
            if res["code"]==200:
                assert 'token' in res["data"],"没有token"

    @pytest.mark.order(2)
    def test_user_get_info(self,operator_without_auth):
        client=UserApi(operator_without_auth)
        res=client.get_user_info("/sso/info")
        assert res.status_code==200
        res=res.json()
        assert res["code"]==401
        assert res["message"]=="暂未登录或token已经过期"

    @pytest.mark.order(3)
    @ddt("data_get_info.yaml")
    def test_user_get_info_success(self,operator_with_auth,data):
        client=UserApi(operator_with_auth)
        res=client.get_user_info("/sso/info")
        assert res.status_code==200
        res=res.json()
        assert res["code"]==data["expected"]["code"]
        assert res["message"]==data["expected"]["message"]

    def test_user_logout(self,operator_with_auth):
        client=UserApi(operator_with_auth)
        res=client.logout("/sso/logout")
        assert res.status_code==200
        res=res.json()
        assert res["code"]==200
        assert res["message"]=="操作成功"

    def test_modify_password(self,operator_with_auth):
        client=UserApi(operator_with_auth)
        res=client.modify_password("")
