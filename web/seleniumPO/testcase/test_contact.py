import pytest
import yaml

from web.seleniumPO.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainPage = MainPage()

    #参数化联系人信息，数据从data.yaml处获取
    @pytest.mark.parametrize(("username", "account","phonenum"), yaml.safe_load(open("../data/data.yaml")))
    def test_contact(self,username,account,phonenum):
        page = self.mainPage.goto_add_member()
        #添加联系人
        page.add_member(username,account,phonenum)
        #获取联系人列表数据，包括下一页联系人
        names = page.get_allMember()
        print(names)
        #断言添加的联系人存在列表里
        assert username in names

    #测试点击下一页功能，并获取下一页页数
    def test_nextPage(self):
        textPage = self.mainPage.goto_member().get_Page()
        #断言当前页数
        assert  textPage =='2/3'