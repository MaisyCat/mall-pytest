from common.request_util import RequestUtil


class UserApi:
    """
    用户接口类
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client


    # 登录接口
    def login(self,endpoint:str,username:str,password:str):
        return self.request_util.send("post",endpoint,data={"username":username,"password":password})
    # 获取用户信息接口
    def get_user_info(self,endpoint:str):#在线测试的时候，这个接口需要登录
        return self.request_util.send("get",endpoint)
    # 登出接口
    def logout(self,endpoint:str):#在线测试的时候，这个接口需要登录
        return self.request_util.send("post",endpoint)
    # 注册接口
    def register(self,endpoint:str,username:str,password:str,telephone:str,authCode:str):
        return self.request_util.send("post",endpoint,data={"username":username,"password":password,"telephone":telephone,"authCode":authCode})
    # 修改密码接口 需登录
    def modify_password(self,endpoint:str,telephone:str,password:str,authCode:str):
        return self.request_util.send("post",endpoint,data={"telephone":telephone,"password":password,"authCode":authCode})
    # 获取手机验证码接口
    def get_auth_code(self,endpoint:str,telephone:str):
        return self.request_util.send("get",endpoint,data={"telephone":telephone})
    # 添加收藏商品
    def add_product_collection(self,endpoint:str,memberProductCollection:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=memberProductCollection)
    # 删除收藏列表
    def delete_collection(self, endpoint:str, productId:int):
        return self.request_util.send("post",endpoint,params={"productId":productId})
    # 清空收藏商品
    def clear_collection(self, endpoint:str):
        return self.request_util.send("post",endpoint)
    # 显示收藏列表
    def get_collection(self, endpoint:str, pageNum:int, pageSize:int):
        return self.request_util.send("get",endpoint,params={"pageNum":pageNum,"pageSize":pageSize})
    # 显示收藏商品详情
    def get_collection_detail(self,endpoint:str,productId:int):
        return self.request_util.send("get",endpoint,params={"productId":productId})
    # 分页获取浏览记录
    def get_read_history(self,endpoint:str,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"pageNum":pageNum,"pageSize":pageSize})
    # 创建浏览记录
    def create_read_history(self,endpoint:str,memberReadHistory:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=memberReadHistory)
#     删除浏览记录
    def delete_read_history(self,endpoint:str,ids:list):
        return self.request_util.send("post",endpoint,json=ids)
    # 清空浏览记录
    def clear_read_history(self,endpoint:str):
        return self.request_util.send("post",endpoint)
    # 添加收货地址
    def add_address(self,endpoint:str,umsMemberReceiveAddress:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=umsMemberReceiveAddress)
    # 删除收货地址
    def delete_address(self, endpoint:str, addressId:int):
        return self.request_util.send("post", endpoint, params={"id":addressId})
    # 修改收货地址
    def update_address(self,endpoint:str,umsMemberReceiveAddress:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=umsMemberReceiveAddress)
    # 显示所有收货地址
    def get_all_address(self,endpoint:str):
        return self.request_util.send("get",endpoint)
    # 显示收货地址详情
    def get_address_detail(self,endpoint:str,addressId:int):
        return self.request_util.send("get",endpoint,params={"id":addressId})
    # 用户取消订单
    def cancel_order(self,endpoint:str,orderId:int):
        return self.request_util.send("post",endpoint,params={"orderId":orderId})
    # 用户确认收货
    def confirm_receive(self,endpoint:str,orderId:int):
        return self.request_util.send("post",endpoint,params={"orderId":orderId})
    # 用户删除订单
    def delete_order(self,endpoint:str,orderId:int):
        return self.request_util.send("post",endpoint,params={"orderId":orderId})
    # 按状态分页获取用户订单
    def get_order_list(self,endpoint:str,status:int,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"status":status,"pageNum":pageNum,"pageSize":pageSize})
