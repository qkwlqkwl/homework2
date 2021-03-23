from homework.appium_work1.pages.base_page import BasePages
from homework.appium_work1.pages.showPersonalInformation_page import ShowPersonnalInformationPage


class PersonalInformationPage(BasePages):
    #进入编辑个人信息页面，点击右上角进入下一页
    def goto_editPersonalInformation_page(self):
        self.parse_action("../pages/personalInformation_page.yaml", "goto_editPersonalInformation_page")
        return ShowPersonnalInformationPage(self.driver)
