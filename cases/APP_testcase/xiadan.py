from appium import webdriver
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
from lib.app_public import *
from lib.config import *
from Page import JXS_APP_PaGe

login()
wd = GSTORE['wd']

class zd00001():

    name = '下单'

    def teststeps(self):
        #点击商城
        shangcheng = JXS_APP_PaGe.ShangCheng_page(wd)
        shangcheng.dianjishangcheng()
        #搜索商品
        shangcheng.chaxunshangpin('贵妇美颜膏')
        #点击商品
        sleep(2)
        wd.tap([(198, 566)], 100)
        # shangcheng.dianjishangpin()
        #点击下单
        shangpinxiangqing = JXS_APP_PaGe.ShangPinXangQing_page(wd)
        shangpinxiangqing.xiadan()
        #选择收货地址
        jiesuanzhongxin = JXS_APP_PaGe.JieSuanZhongXin_page(wd)
        sleep(2)
        wd.tap([(500, 350)], 100)
        sleep(2)
        wd.tap([(500, 2100)], 100)
        jiesuanzhongxin.tijiaodingdan()
        jiesuanzhongxin.panduanshifouchengong()
