from homework.appium_work1.pages.base_page import BasePages
from homework.appium_work1.pages.maillist_page import MaillistPage

class InformationPage(BasePages):

    #信息页面，点击通讯录，进入通讯录页面
    def goto_maillist_page(self):
        #数据驱动，点击通讯录，进入通讯录页面
        self.parse_action("../pages/information_page.yaml","goto_maillist_page")
        return MaillistPage(self.driver)