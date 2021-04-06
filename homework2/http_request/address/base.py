import requests

class Base:
    def __init__(self):
        #使用session
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token":self.token}
    #封装send方法
    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)
    #获取token
    def get_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwcb9682d77870cab9&corpsecret=CnSJ-l_dT5gu0VzZnAMC2h5uGr3KUCSqaai_bryyr9c')
        #assert 0 == r.json()['errcode']
        token = r.json()['access_token']
        return token