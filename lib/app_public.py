from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

from selenium.webdriver.common.by import By
from lib.config import configs
from hytest import *
from Page.LoginPage import login_page


def app_lianjie(appPackage, appActivity):
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '10',  # 手机安卓版本
        'deviceName': 'TEL-AN00a',  # 设备名，安卓手机可以随意填写
        'appPackage': appPackage,  # 启动APP Package名称
        'appActivity': appActivity,  # 启动Activity名称
        # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2',
        'chromeOptions': {'w3c': False}
        # 'app': r'd:\apk\bili.apk',
    }
    return desired_caps


def login(url=configs.url, vcode=configs.vcode):
    desired_caps = app_lianjie('com.mageline.agent', '.ui.MainActivity')
    # desired_caps = app_lianjie('com.tencent.mm', '.ui.LauncherUI')
    wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    GSTORE['wd'] = wd
    wd.implicitly_wait(8)
    loginpage = login_page(wd)
    #跳过开平动画
    sleep(1)
    wd.tap([(929, 161)], 100)
    # wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
    #                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View'
    #                                 '/android.view.View/android.view.View/android.view.View/android.view.View['
    #                                 '1]/android.widget.EditText[1]').click()
    # wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
    #                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View'
    #                                 '/android.view.View/android.view.View/android.view.View/android.view.View['
    #                                 '1]/android.widget.EditText[1]').send_keys('123123')
    #输入账号
    loginpage.shuruzhanghao('18090930111')
    # 输入密码
    loginpage.shurumima('123456')
    #勾选协议
    loginpage.gouxuanxieyi()
    # # 点击登录
    loginpage.dianjidenglu()
    sleep(10)


login()
