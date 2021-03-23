from homework.appium_work1.pages.base_page import BasePages


class DeletePersonalInformationPage(BasePages):
    #删除成员
    def deleteMember(self):
        self.parse_action("../pages/deletePersonalInformation_page.yaml", "deleteMember")