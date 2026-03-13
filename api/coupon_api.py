from common.request_util import RequestUtil


class CouponApi:
    """
    优惠券接口类
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client
    # 领取指定优惠券
    def receive_coupon(self,endpoint:str,couponId:int):
        return self.request_util.send("post",endpoint,params={"couponId":couponId})
    # 获取用户优惠券列表
    def get_user_coupon_list(self,endpoint:str,useStatus:int):
        return self.request_util.send("get",endpoint,params={"useStatus":useStatus})
    # 获取用户优惠券历史列表
    def get_user_coupon_history_list(self,endpoint:str,useStatus:int):
        return self.request_util.send("get",endpoint,params={"useStatus":useStatus})
    # 获取当前商品相关优惠券
    def get_product_related_coupon(self,endpoint:str,productId:int):
        return self.request_util.send("get",endpoint,params={"productId":productId})
    # 获取登录用户购物车的相关优惠券
    def get_cart_related_coupon(self,endpoint:str,Type:int):
        return self.request_util.send("get",f'{endpoint}/{Type}')
