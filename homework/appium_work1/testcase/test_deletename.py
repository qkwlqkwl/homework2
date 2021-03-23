from time import sleep

from homework.appium_work1.pages.app import App


class TestDeleteName:
    def setup(self):
        self.app = App()

    def test_deletename(self):
        #username保存删除的联系人姓名，用来传参
        username='username004'
        #定义一个delete_bef,保存删除之前的人数
        delete_bef = []
        #定义一个delete_aft，保存删除之后的人数
        delete_aft = []
        ele = self.app.goto_main().goto_maillist_page().goto_searchname_page()
        #查找username的个数
        delete_bef = ele.searchname(username)
        #删除username
        ele.goto_Personalinformation_page(username).goto_editPersonalInformation_page().goto_deletePersonalInformationPage().deleteMember()
        #再次查找username的个数
        delete_aft = ele.searchname(username)
        #断言删除后的联系人个数比删除前少
        assert len(delete_bef)>len(delete_aft)
