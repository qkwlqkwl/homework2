import requests

from homework2.http_request.address.base import Base


class Address(Base):

    #查询成员
    def get_member_information(self,user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            # "access_token": self.token,
            "userid": user_id
        }
        #r = self.s.get(get_member_url,params=params)
        r = self.send("GET",get_member_url, params=params)
        #assert 'aaa001002'== r.json()["name"]
        return r.json()

    #更新成员
    def update_member(self,user_id,name,mobile):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid":user_id,
            "name":name,
            "mobile":mobile
        }
        #r = self.s.get(url=update_member_url,json=data)
        r = self.send("GET", update_member_url, json=data)
        print(r.json())
        return r.json()

    #新建成员
    def creat_member(self,user_id,name,mobile,department):
        creat_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
        "userid": user_id,
        "name": name,
        "mobile": mobile,
        "department": department
        }
        #r = self.s.post(url=creat_member_url,json=data)
        r = self.send("POST", creat_member_url, json=data)
        return r.json()
    #删除成员
    def delete_member(self,userid):
        #delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid={userid}"
        delete_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "access_token":self.token,
            "userid":userid
        }
        #r = self.s.get(delete_member_url,params=params)
        r = self.send("POST", delete_member_url, params=params)
        return r.json()

    # 批量删除成员
    def batch_delete_member(self, useridlist):
        batch_delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token={self.token}"
        data = {
            "useridlist": useridlist
        }
        r = self.send("POST", batch_delete_member_url, json=data)
        return r.json()

    # 获取部门成员
    def get_department_member(self,department):
        department_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist"
        params = {
            "access_token": self.token,
            "department_id": department,
            "fetch_child": 0
        }
        r = self.send("GET", department_member_url, params=params)
        #print(r.json())
        return r.json()

