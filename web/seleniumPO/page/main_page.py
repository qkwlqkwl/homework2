#企业微信主页
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.seleniumPO.page.add_member_page import AddMemberPage
from web.seleniumPO.page.base_page import BasePage


class MainPage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        #点击添加成员
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)

    def goto_member(self):
        """
        添加成员
        :return:
        """
        #点击添加成员
        self.driver.find_element(By.ID,"menu_contacts").click()
        return AddMemberPage(self.driver)
