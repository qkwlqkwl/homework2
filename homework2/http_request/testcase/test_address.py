import pytest

from homework2.http_request.address.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = "zhangsan00123"
        self.name = "张三"
        self.mobile = "+86 13811112222"
        self.department = [1]
        self.useridlist = ["lisi001", "lisi002"]
        self.mobilelist = ["13988880001", "13988880002"]

    @pytest.mark.parametrize("user_id,mobile",[("zhangsan001","13988884410"),
                                               ("zhangsan002","13988884422"),
                                               ("zhangsan003","13988884433"),
                                               ("zhangsan004","13988884444"),
                                               ("zhangsan005","13988884455"),
                                               ("zhangsan006","13988884466"),
                                               ("zhangsan007","13988884477"),
                                               ("zhangsan008","13988884488")])
    def test_create_member(self,user_id,mobile):
        self.address.delete_member(user_id)
        r = self.address.creat_member(user_id,self.name,mobile,self.department)
        #self.address.delete_member(self.user_id)
        #r['orrmsg'] == "create" #如果没有值会抛异常
        #r.get('errmsg',"network error")方式，会抛出指定错误
        assert r.get('errmsg',"network error") == "created"
        r = self.address.get_member_information(user_id)
        assert r.get("name") == self.name

    def test_get_member_information(self):
        r = self.address.get_member_information(self.user_id)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == self.name

    def test_delete_member(self):
        self.address.creat_member(self.user_id,self.name,self.mobile,self.department)
        r = self.address.delete_member(self.user_id)
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member_information(self.user_id)
        assert r.get("errcode") == 60111

    def test_update_member(self):
        self.address.creat_member(self.user_id, self.name, self.mobile, self.department)
        new_name=self.name + "tmp"
        r = self.address.update_member(self.user_id,new_name,self.mobile)
        print(r)
        assert r.get("errmsg") == "updated"
        r = self.address.get_member_information(self.user_id)
        assert r.get("name") == new_name

    #测试批量删除成员接口
    def test_batch_delete_member(self):
        #删除已存在的旧数据
        for userid in self.useridlist:
            self.address.delete_member(userid)
        #循环创建成员
        for i in range(2):
            self.address.creat_member(self.useridlist[i], self.name, self.mobilelist[i], self.department)
        #批量删除成员
        r = self.address.batch_delete_member(self.useridlist)
        print(r)
        assert r.get("errmsg") == "deleted"

    #获取部门成员
    def test_get_department_member(self):
        #定义空列表
        userid_list=[]
        #获取返回的成员信息
        r = self.address.get_department_member(self.department)
        #断言返回成功
        assert r.get("errmsg") == "ok"
        userlists:list[dict] = r['userlist']
        #遍历部门成员，取出userid
        for userlist in userlists:
            userid_list.append(userlist["userid"])
        #断言部门成员里有设置的self.user_id="zhangsan00123"
        assert self.user_id in userid_list






