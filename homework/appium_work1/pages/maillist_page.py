from homework.appium_work1.pages.addmember_page import AddMemberPage
from homework.appium_work1.pages.base_page import BasePages


class MaillistPage(BasePages):
    #通讯录页面，滚动查找添加成员元素
    def goto_addmember_page(self):
        # 滚动查找元素，找到后点击进入添加成员页面
        self.swip_click("添加成员")
        return AddMemberPage(self.driver)
