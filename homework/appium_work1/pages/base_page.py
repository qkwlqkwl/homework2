import yaml
from selenium.webdriver.remote.webdriver import WebDriver
class BasePages:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def find_click(self,locator):
        self.find(locator).click()

    def find(self,locator):
        return self.driver.find_element_by_xpath(locator)
    def findId(self,locator):
        return self.driver.find_element_by_id(locator)
    def findId_click(self,locator):
        return self.findId(locator).click()

    def swip_click(self,text):
        # 滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                                        'instance(0));').click()

    def parse_action(self,path,fun_name):
        with open(path,"r",encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps:list[dict]= function[fun_name]
        for step in steps:
            if step["action"]=="find_click":
                self.find_click(step["locator"])
            elif step["action"]=="find":
                self.find(step["locator"])
            elif step["action"]=="send_key":
                self.findId(step["locator"]).send_keys(step["value"])
            elif step["action"]=="findId_click":
                self.findId_click(step["locator"])


