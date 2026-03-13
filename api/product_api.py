from common.request_util import RequestUtil


class ProductApi:
    """
    首页展示商品资源
    """
    def __init__(self,client:RequestUtil):
        self.request_util=client
    # 主页面信息加载
    def home_content(self,endpoint:str):
        return self.request_util.send("get",endpoint)
    # 热门商品分页加载
    def get_hot_product_list(self,endpoint:str,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"pageNum":pageNum,"pageSize":pageSize})
    # 新鲜好物分页加载
    def get_new_product_list(self,endpoint:str,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"pageNum":pageNum,"pageSize":pageSize})
    # 推荐商品分页加载
    def get_recommend_product_list(self,endpoint:str,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"pageNum":pageNum,"pageSize":pageSize})
    # 首页商品分类
    def get_case(self,endpoint:str,parentId:int):
        return self.request_util.send("get",f"{endpoint}/{parentId}")
    # 根据分类id获取专题
    def get_subject_by_case(self,endpoint:str,caseId:int,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"caseId":caseId,"pageNum":pageNum,"pageSize":pageSize})
    # 前台商品详情
    def get_product_detail(self,endpoint:str,productId:int):
        return self.request_util.send("get", f"{endpoint}/{productId}")
    # 商品搜索
    def common_search(self,endpoint:str,keyword:str,brandId:int,productCategoryId:int,pageNum:int,pageSize:int):
        return self.request_util.send("get",endpoint,params={"keyword":keyword,"brandId":brandId,"productCategoryId":productCategoryId,"pageNum":pageNum,"pageSize":pageSize})
    # 商品分类树
    def get_product_cate_by_tree(self,endpoint:str):
        return self.request_util.send("get",endpoint)

