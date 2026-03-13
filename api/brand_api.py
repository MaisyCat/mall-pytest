from common.request_util import RequestUtil


class BrandApi:
    """
    品牌接口类
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client

    # 分页获取品牌
    def get_brand(self, endpoint: str, pageNum: int, pageSize: int):
        return self.request_util.send("get", endpoint, params={"pageNum": pageNum, "pageSize": pageSize})

    # 根据品牌id获取商品
    def get_product_by_brand(self, endpoint: str, brandId: int, pageNum: int, pageSize: int):
        return self.request_util.send("get", endpoint,params={"brandId": brandId, "pageNum": pageNum, "pageSize": pageSize})

    # 获取品牌详情
    def get_brand_detail(self, endpoint: str, brandId: int):
        return self.request_util.send("get", f"{endpoint}/{brandId}")

