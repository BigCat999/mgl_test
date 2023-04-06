from selenium.webdriver.common.by import By
from Page.BasePage import Page
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from hytest import *


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

    # 协议按钮
    xieyi = (AppiumBy.CLASS_NAME, 'android.widget.CheckBox')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def shuruzhanghao(self, zhanghao):
        print('输入账号')
        self.click(self.zhanghao)
        self.sendkeys(self.zhanghao, zhanghao)

    def shurumima(self, mima):
        print('输入密码')
        self.click(self.mima)
        self.sendkeys(self.mima, mima)

    def dianjidenglu(self):
        print("点击登录按钮")
        self.click(self.hot_search)

    def gouxuanxieyi(self):
        print("勾选协议")
        self.click(self.xieyi)


# 商城page
class ShangCheng_page(Page):
    # 商城菜单
    shangchengcaidan = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="商城, 第 3 个标签，共 5 个"]')
    # 搜索框
    sousuokuang = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="请输入商品名称"]')
    # 二级搜索框
    erjisousuokuang = (
    AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                    '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                    '.View/android.view.View/android.view.View/android.view.View/android.widget'
                    '.EditText')

    # 查询
    chaxun = (AppiumBy.XPATH, '//android.view.View[@content-desc="搜索"]')
    # 购物车
    gouwuche = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View'
                                '/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]')
    # 商品
    shangpin = (AppiumBy.XPATH, '//android.view.View[@content-desc="贵妇美颜膏 ¥302.68"]/android.widget.ImageView[1]')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def dianjishangcheng(self):
        sleep(3)
        self.click(self.shangchengcaidan)

    def chaxunshangpin(self, shangpinming):
        self.click(self.sousuokuang)
        sleep(1)
        self.click(self.erjisousuokuang)
        sleep(1)
        self.sendkeys(self.erjisousuokuang, shangpinming)
        sleep(1)
        self.click(self.chaxun)

    def dianjishangpin(self):
        self.click(self.shangpin)


# 商品详情page
class ShangPinXangQing_page(Page):
    # 选择数量
    shuliangkuang = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')
    # 查询
    chaxun = (AppiumBy.XPATH, '//android.view.View[@content-desc="搜索"]')
    # 输入数量
    shurushuliang = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                     '/android.view.View/android.view.View/android.view.View['
                                     '1]/android.view.View/android.widget.EditText')

    # 确定购买数量
    queding = (AppiumBy.ID, '确定')

    # 提货权限
    tihuoquanxian = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')

    jiagou = (AppiumBy.ID, '加入购物车')

    xiadananniu = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="立即下单"]')

    chakangouwuche = (AppiumBy.ID, '购物车')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def xuanzeguige(self, guige):
        guige = (AppiumBy.ID, guige)
        self.click(guige)

    def xuanzegoumainum(self, num):
        self.click(self.shurushuliang)
        self.sendkeys(self.queding, num)
        self.click(self.queding)

    def tihuoquanxianxuanze(self, tihuoquanxian):
        tihuoquanxian = (AppiumBy.ID, tihuoquanxian)
        self.click(self.tihuoquanxian)

    def jiagou(self):
        self.click(self.jiagou)

    def jinrugouwuche(self):
        self.click(self.chakangouwuche)

    def xiadan(self):
        sleep(2)
        self.click(self.xiadananniu)


# 购物车page
class GouWuChe_page(Page):
    # 选择订单
    xuanzedingdan = (AppiumBy.ID, '日常订购商品')
    # 下单
    xiadan = (AppiumBy.ID, '去下单')

    def __init__(self, wd):
        Page.__init__(self, wd)

    def xuanzeshangpin(self):
        self.click(self.xuanzedingdan)

    def xiadan(self):
        self.click(self.xiadan)


# 结算中心page
class JieSuanZhongXin_page(Page):
    # 收货地址
    xuanzedingdan = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="收货地址 请选择收货人和收货地址"]')
    # 提交订单
    tijiaodingdananniu = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="提交订单"]')
    # 常用地址
    dizhi = (AppiumBy.ACCESSIBILITY_ID, 'B类线上 15447475858 上海市上海市嘉定区安亭镇963')
    # 提交成功
    tijiaowenan = (AppiumBy.XPATH, '//android.view.View[@content-desc="订单提交成功"]')

    def __init__(self, wd):
        Page.__init__(self, wd)

    # 提交订单
    def tijiaodingdan(self):
        sleep(2)
        self.click(self.tijiaodingdananniu)

    # 选择收货地址
    def xuanzedizhi(self):
        self.click(self.xuanzedingdan)
        self.click(self.dizhi)

    # 判断是否提交成功
    def panduanshifouchengong(self):
        sleep(3)
        text = self.get_attribute('content-desc	', self.tijiaowenan)
        INFO(f'提交文案{text}')
        CHECK_POINT('是否提交成功', text == '订单提交成功')
