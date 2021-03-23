from homework.appium_work1.pages.addmember_page import AddMemberPage
from homework.appium_work1.pages.base_page import BasePages
from homework.appium_work1.pages.search_name import SearchNamePage


class MaillistPage(BasePages):
    #通讯录页面，滚动查找添加成员元素
    def goto_addmember_page(self):
        # 滚动查找元素，找到后点击进入添加成员页面
        self.parse_action("../pages/maillist_page.yaml","goto_addmember_page")
        return AddMemberPage(self.driver)

    #通讯录页面，点击右上角的搜索按钮，进入搜索页面
    def goto_searchname_page(self):
        self.parse_action("../pages/maillist_page.yaml","goto_searchname_page")
        return SearchNamePage(self.driver)
