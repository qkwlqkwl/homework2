from appium import webdriver
from homework.appium_work1.pages.information_page import InformationPage

class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        #设置企业微信连接信息
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 设置动态页面的等待时间为0秒
        caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(4)

    #进入信息页
    def goto_main(self):
        return InformationPage(self.driver)