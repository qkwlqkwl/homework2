import json


import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
import logging

root_log = logging.getLogger(__name__)
for h in root_log.handlers[:]:
    root_log.removeHandler(h)
    h.close()

logging.basicConfig(level=logging.INFO,
                    #日志个数，时间，代码所在文件名，文件名，代码行号，日志级别名字，日志
                    format='%(asctime).19s %(filename)s[line:%(lineno)d] %(levelname)s %(message).100s',
                    #打印日志的时间
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    #日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    #打开日志文件的方式
                    filemode='w')



class BasePages:
    _error_num=0
    _max_num=3
    # 定义一个字典，要替换的内容放在字典里
    _params = {}
    _blacklist=[(MobileBy.XPATH,"//*[@text='待办' and @resource-id='com.tencent.wework:id/ig1'] /../../../..//*[@resource-id='com.tencent.wework:id/ig0']")]


    def __init__(self,driver: WebDriver = None):
        self.driver = driver

    def find(self,by,locator):
        logging.info(f"find: by={by},locator = {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            return element
        except Exception as e:
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png",attachment_type=allure.attachment_type.PNG)
            # 处理黑名单逻辑
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素的列表[ele1,ele2.....]，如果没有元素会返回一个空列表
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

    def find_click(self,by,locator):
        self.find( by,locator).click()

    def finds(self,by,locator):
        # elements = self.driver.find_elements(by, locator)
        # return elementStyle
        try:
            elements = self.driver.find_elements(by, locator)
            self._error_num = 0
            return elements
        except Exception as e:
            # 处理黑名单逻辑
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素的列表[ele1,ele2.....]，如果没有元素会返回一个空列表
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.finds(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e


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

        # json序列化与反序列化
        # json.dumps()序列化
        # json.loads()反序列化
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"]=="find_click":
                self.find_click(step["by"],step["locator"])
            elif step["action"]=="find":
                self.find(step["by"],step["locator"])
            elif step["action"]=="send_keys":
                self.find(step["by"],step["locator"]).send_keys(step["value"])
            elif step["action"]=="swip_click":
                self.swip_click(step["value"])
            elif step["action"]=="finds_click":
                self.finds(step["by"],step["locator"])[0].click()
            elif step["action"]=="finds":
                return self.finds(step["by"],step["locator"])


