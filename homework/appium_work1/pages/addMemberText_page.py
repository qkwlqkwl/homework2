from homework.appium_work1.pages.base_page import BasePages

class AddMemberTextPage(BasePages):
    #添加成员详情页，文本框输入姓名，手机号，点击保存按钮，添加成功
    def addMemberText(self):
        self.parse_action("../pages/addMemberText_page.yaml", "addMemberText")

    def varity_ok(self):
        self.parse_action("../pages/editcontact_page.yaml", "varity_ok")





