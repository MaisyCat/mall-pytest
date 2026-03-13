from common.request_util import RequestUtil


class OrderApi:
    """
    订单接口类
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client

    # 根据购物车ids列表生成确认单
    def generate_confirm_order(self,endpoint:str,integers:list[int]):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=integers)
    # 根据购物车信息生成订单
    def generate_order(self,endpoint:str,orderParam:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=orderParam)
    # 获取订单详情byid
    def get_order_detail(self,endpoint:str,orderId:int):
        return self.request_util.send("get",f'{endpoint}/{orderId}')

    # 自动取消超时订单
    def cancel_time_out_order(self,endpoint:str):
        return self.request_util.send("post",endpoint)
    # 取消单个超时订单
    def cancel_order(self,endpoint:str,orderId:int):
        return self.request_util.send("post",endpoint,params={"orderId":orderId})
    # 用户支付成功的回调
    def pay_success(self,endpoint:str,orderId:int,payType:int):
        return self.request_util.send("post",endpoint,params={"orderId":orderId,"payType":payType})
    
