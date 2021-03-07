import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenium.base import Base


class TestDemo():
    def setup_method(self,method):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        #复用浏览器地址，需要提前打开页面,绕开登录操作
        #self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown_method(self):
        #self.driver.quit()
        pass

    def test_cookie(self):
        #get_cookies()#获取当前页面的cookis
        #cookies = self.driver.get_cookies()
        #print(cookies)
        #打开index页面，需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #带有登录信息的cookie
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853852205579'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Dq_xqAUzfhjGlVYit5Bi2RxGciHCjnz5HcUqDRfukXQKmE_3TTE0aGWzdju_wl5V-hnaZXAyxh_0JFmHYMpNCivnMGvbVN92laLx2JAWwLgkjRa6KlJ3RSh3MopCqjuBbSASPEp9VjJRi2UecRWeBCQZ4OruWL-sXQezPd0asgR-LB45Isgrl3fVRVbMk6uW2ctDvGSzfPtb2w50cgDSV81LsJ9_dBSJnfbPtlKhqYDz7_I3C6Ve_BWvMgXoTKEi5nfiKbj22Ci1BAgF5LYwxg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853852205579'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325062420327'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'gXLpcjFPZducd5lxkSbx1GBmQfAfaPHxUbm2j5QS-_xKN0iDUEyEAyqdq432Sci3'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7815832'}, {'domain': '.qq.com', 'expiry': 1615128194, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com', 'expiry': 1615154913, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7fbb7im'}, {'domain': '.qq.com', 'expiry': 1615214566, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1784827452.1615123379'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1615128133'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '13764506182530248'}, {'domain': '.qq.com', 'expiry': 1678200166, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1424260045.1614180679'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645716677, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1617720169, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646664133, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1615123378,1615123828,1615127484,1615128133'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '916562086'}, {'domain': '.qq.com', 'expiry': 1925107743, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_54079a51ba78f'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '3bdb73bc4284068f327ed439f2491ca6f0a0a3bbae664643cb62ebda2c856452'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'tGbQaJfGEt'}]
        #cookies = self.driver.get_cookies()
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
                #add_cookie()只能加入字典，所以需要遍历列表里的字典，再加入add_cookie()
            self.driver.add_cookie(cookie)
        #获取cookie后，再次打开页面，进入已登录状态
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)
        #鼠标滚动1000
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        #获取并点击导入通讯录元素
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        #上传文件
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("C:/Users/Jingjing/Desktop/202012121.xls")
        #获取文件名称
        file_name = self.driver.find_element_by_id("upload_file_name").text
        #断言是否上传成功
        assert file_name == "202012121.xls"
        sleep(2)

    #实现cookie数据的持久化存储
    def test_shelve(self):
        #shelve python内置的模块，相当于小型的数据库
        #带有登录信息的cookie
        db= shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
                #add_cookie()只能加入字典，所以需要遍历列表里的字典，再加入add_cookie()
            self.driver.add_cookie(cookie)
        #获取cookie后，再次打开页面，进入已登录状态
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(2)
        #鼠标滚动1000
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        #获取并点击导入通讯录元素
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        #上传文件
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("C:/Users/Jingjing/Desktop/202012121.xls")
        #获取文件名称
        file_name = self.driver.find_element_by_id("upload_file_name").text
        #断言是否上传成功
        assert file_name == "202012121.xls"
        sleep(2)

