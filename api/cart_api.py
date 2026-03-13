from common.request_util import RequestUtil


class  CartApi:
    """
    购物车接口类
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client
    # 携带token
    # 添加商品到购物车
    def add_cart(self,endpoint:str,omsCartItem:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post",endpoint,json=omsCartItem)
    # 携带token
    # 获取购物车列表
    def get_cart_list(self,endpoint:str):
        return self.request_util.send("get",endpoint)
    # 携带token
    # 获取会员购物车中商品促销信息
    def get_cart_list_promotion(self,endpoint:str,cartIds:list[int]):
        return self.request_util.send("get", endpoint, params={"cartIds": cartIds})
    # 获取购物车中某个规格
    def get_product_specification(self,endpoint:str,productId:int):
        return self.request_util.send("get", f"{endpoint}/{productId}")
    # 修改某个商品的数量
    def update_quantity(self,endpoint:str,productId:int,quantity:int):
        return self.request_util.send("get", endpoint, params={"id":productId,"quantity": quantity})
    # 清除购物车
    def clear_cart(self,endpoint:str):
        return self.request_util.send("post", endpoint)
    # 删除购物车商品
    def delete_cart_item(self,endpoint:str,ids:list[int]):
        return self.request_util.send("post", endpoint, json=ids)
    # 修改商品规格
    def update_product_specification(self,endpoint:str,omsCartItem:list):
        self.request_util.session.headers["Content-Type"] = "application/json;charset=utf-8"
        return self.request_util.send("post", endpoint, json=omsCartItem)
