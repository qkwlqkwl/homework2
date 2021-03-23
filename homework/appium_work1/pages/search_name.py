from homework.appium_work1.pages.base_page import BasePages

from homework.appium_work1.pages.personalInformation_page import PersonalInformationPage


class SearchNamePage(BasePages):
    #搜索框搜索username,点击返回的第一个username,进入个人信息页面
    def goto_Personalinformation_page(self,username):
        self._params['username'] = username
        self.parse_action("../pages/search_name.yaml", "goto_Personalinformation_page")
        return PersonalInformationPage(self.driver)

    #搜索框搜索username，返回查到的列表
    def searchname(self,username):
        self._params['username'] = username
        return self.parse_action("../pages/search_name.yaml", "searchname")

