from selenium.webdriver.common.by import By
from Page.BasePage import Page
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 商品详情page
class ShangPinXangQing_page(Page):

    # 选择数量
    shuliangkuang = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')
    # 查询
    chaxun = (AppiumBy.XPATH, '//android.view.View[@content-desc="搜索"]')
    #输入数量
    shurushuliang = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                     '/android.view.View/android.view.View/android.view.View['
                                     '1]/android.view.View/android.widget.EditText')

    #确定购买数量
    queding = (AppiumBy.ID, '确定')

    #提货权限
    tihuoquanxian = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')

    jiagou = (AppiumBy.ID, '加入购物车')

    xiadan = (AppiumBy.ID, '立即下单')

    chakangouwuche = (AppiumBy.ID, '购物车')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def xuanzeguige(self,guige):
        guige = (AppiumBy.ID, guige)
        self.click(guige)

    def xuanzegoumainum(self, num):
        self.click(self.shurushuliang)
        self.sendkeys(self.queding, num)
        self.click(self.queding)

    def tihuoquanxianxuanze(self,tihuoquanxian):
        tihuoquanxian = (AppiumBy.ID, tihuoquanxian)
        self.click(self.tihuoquanxian)

    def jiagou(self):
        self.click(self.jiagou)

    def jinrugouwuche(self):
        self.click(self.chakangouwuche)

    def xiadan(self, xiadan):
        self.click(self.xiadan)