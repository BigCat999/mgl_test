from selenium.webdriver.common.by import By
from Page.BasePage import Page
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 商城page
class ShangCheng_page(Page):
    # 商城菜单
    shangchengcaidan = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="商城, 第 3 个标签，共 5 个"]')
    # 搜索框
    sousuokuang = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="请输入商品名称"]')
    # 查询
    chaxun = (AppiumBy.XPATH, '//android.view.View[@content-desc="搜索"]')
    #购物车
    gouwuche = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def dianjishangcheng(self,zhanghao):
        self.click(self.shangchengcaidan)
        self.sendkeys(self.zhanghao, zhanghao)

    def chaxunshangpin(self,mima):
        self.click(self.sousuokuang)
        self.sendkeys(self.sousuokuang, mima)
        self.click(self.chaxun)

    # def dianjidenglu(self):
    #     print("点击登录按钮")
    #     self.click(self.hot_search)
    #
    # def gouxuanxieyi(self):
    #     print("勾选协议")
    #     self.click(self.xieyi)
    # def input_search_text(self, text="testerGuie"):
    #     print("输入搜索关键字：测试开发Guide")
    #     self.input_text(self.search_input, text)
    #
    # def click_search_btn(self):
    #     print("点击 百度一下  按钮")
    #     self.click(self.search_button)
    #
    # def get_hot_search_title(self):
    #     return self.get_attribute("title",self.hot_search)