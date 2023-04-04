from selenium.webdriver.common.by import By
from Page.BasePage import Page
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 购物车page
class GouWuChe_page(Page):

    # 选择订单
    xuanzedingdan = (AppiumBy.ID, '日常订购商品')
    # 下单
    xiadan = (AppiumBy.ID, '去下单')
    # #输入数量
    # shurushuliang = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
    #                                  '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
    #                                  '/android.view.View/android.view.View/android.view.View['
    #                                  '1]/android.view.View/android.widget.EditText')
    #
    # #确定购买数量
    # queding = (AppiumBy.ID, '确定')
    #
    # #提货权限
    # tihuoquanxian = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')
    #
    # jiagou = (AppiumBy.ID, '加入购物车')
    #
    # xiadan = (AppiumBy.ID, '立即下单')
    #
    # chakangouwuche = (AppiumBy.ID, '购物车')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def xuanzeshangpin(self):
        self.click(self.xuanzedingdan)

    def xiadan(self):
        self.click(self.xiadan)

