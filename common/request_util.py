from operator import truediv

import requests

class RequestUtil:
    def __init__(self,base_url:str):
        self.base_url=base_url
        self.session=requests.session()
        self.token=None

    def send(self,method:str,endpoint:str,**kwargs):
        url=f"{self.base_url}{endpoint}"
        self.session.headers["Content-Type"]="application/x-www-form-urlencoded;charset=utf-8"
        response=self.session.request(method,url,**kwargs)
        return response
    # def get(self,endpoint:str,**kwargs):
    #     return self.send("get",endpoint,**kwargs)
    # def post(self,endpoint:str,**kwargs):
    #     return self.send("post",endpoint,**kwargs)
    # def put(self,endpoint:str,**kwargs):
    #     return self.send("put",endpoint,**kwargs)
    # def delete(self,endpoint:str,**kwargs):
    #     return self.send("delete",endpoint,**kwargs)
    def login(self,username:str,password:str):
        url=f"{self.base_url}/sso/login"
        response=self.session.post(url,data={"username":username,"password":password})
        if response.status_code==200:
            data=response.json()["data"]
            self.token=data["token"]
            self.session.headers["Authorization"]=f"Bearer {self.token}"
            return True
        return False

    def close(self):
        self.session.close()