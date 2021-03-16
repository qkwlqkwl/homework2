from homework.appium_work1.pages.addMemberText_page import AddMemberTextPage
from homework.appium_work1.pages.base_page import BasePages


class AddMemberPage(BasePages):
    #添加成员页面，点击”手动输入添加“
    def addmember(self):
        #数据驱动，点击”手动输入添加“，进入添加成员详情页
        self.parse_action("../pages/addmember_page.yaml","addmember")
        return AddMemberTextPage(self.driver)



