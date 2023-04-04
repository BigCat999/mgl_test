from selenium.webdriver.common.by import By
from Page.BasePage import Page
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 登录页page
class login_page(Page):

    # 账号输入框
    zhanghao = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View'
                                '/android.view.View/android.view.View/android.view.View/android.view.View['
                                '1]/android.widget.EditText[1]')
    # 密码输入框
    mima = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                   '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View'
                   '/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[2]')
    # 登录按钮
    hot_search = (AppiumBy.CLASS_NAME, 'android.widget.Button')

    #协议按钮
    xieyi = (AppiumBy.CLASS_NAME, 'android.widget.CheckBox')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def shuruzhanghao(self,zhanghao):
        print('输入账号')
        self.click(self.zhanghao)
        self.sendkeys(self.zhanghao, zhanghao)

    def shurumima(self,mima):
        print('输入密码')
        self.click(self.mima)
        self.sendkeys(self.mima, mima)

    def dianjidenglu(self):
        print("点击登录按钮")
        self.click(self.hot_search)

    def gouxuanxieyi(self):
        print("勾选协议")
        self.click(self.xieyi)
