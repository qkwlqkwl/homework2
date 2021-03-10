#基类，存放init,find
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            #复用浏览器，需要设置option.debugger_address
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            #创建完driver,理解设置隐式等待
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver
        if self.base_url !="":
            self.driver.get(self.base_url)
            #self.driver.get("")

    def find(self,locator,value):
        return self.driver.find_element(locator,value)
    def finds(self,locator,value):
        return self.driver.find_elements(locator,value)

    def wait_for_click(self,timeout,locator):
         WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator))


