from homework.appium_work1.pages.base_page import BasePages
from homework.appium_work1.pages.deletePersonalInformation_page import DeletePersonalInformationPage


class ShowPersonnalInformationPage(BasePages):
    #进入删除联系人页面
    def goto_deletePersonalInformationPage(self):
        self.parse_action("../pages/showPersonnalInformation_page.yaml", "goto_deletePersonalInformationPage")
        return DeletePersonalInformationPage(self.driver)