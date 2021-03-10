from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from web.seleniumPO.page.base_page import BasePage


class AddMemberPage(BasePage):
    # 类型提示
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    username = "username001"
    account = "username001"
    phonenum = "13011111111"
    def add_member(self,username,account,phonenum):
        """
        添加联系人，详细信息
        :return:
        """
        #输入用户名

        self.find(By.ID,"username").send_keys(username)
        #输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        #输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        #点击保存,当页面属性有多个元素，找到第一个
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return True

    def get_allMember(self):
        """
        获取所有的联系人姓名
        :return:
        """
        #获取复选框元素
        locator = (By.CSS_SELECTOR,".ww_checkbox")
        #等待复选框出现
        self.wait_for_click(10,locator)
        #调用get_nameList()方法，获取当前页联系人信息
        eles_list = self.get_nameList()
        #调用get_currentPage()方法，获取当前页
        currout_page = self.get_currentPage()
        #调用get_totalPages()方法，获取总页数
        totalPage = self.get_totalPages()
        #定义一个联系人列表，用来存放联系人信息
        names = []
        #将第一页的联系人信息存放到列表里
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        #判断当前页小于总页数时，点击下一页操作，并获取下一页联系人信息
        while currout_page<totalPage:
            ele = self.find(By.CSS_SELECTOR, ".js_next_page")
            action = ActionChains(self.driver)
            action.click(ele).perform()
            eles_list = self.get_nameList()
            #继续将下一页的联系人信息存放到names列表里
            for ele in eles_list:
                names.append(ele.get_attribute("title"))
            #重新获取当前页页数
            currout_page = self.get_currentPage()
            #重新获取总页数
            totalPage = self.get_totalPages()
        #返回所有页数的联系人信息
        return names

    #获取当前页的联系人信息
    def get_nameList(self):
        eles_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        return eles_list
    #获取当前页数
    def get_currentPage(self):
        textPage = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        #textPage返回1/3，截取当前页数1
        currentPage = textPage[:textPage.index("/")]
        return currentPage
    #获取总页数
    def get_totalPages(self):
        textPage = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        #textPage返回1/3，截取总页数3
        totalPages = textPage[textPage.index("/") + 1:]
        return totalPages

    #测试点击下一页功能，并获取页数
    def get_Page(self):
        #点击下一页
        ele = self.find(By.CSS_SELECTOR,".js_next_page")
        action = ActionChains(self.driver)
        action.click(ele).perform()
        #获取页数
        textPage = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        return textPage

