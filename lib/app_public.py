from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
import yaml
from selenium.webdriver.common.by import By
from lib.config import configs
from hytest import *
from Page import JXS_APP_PaGe



def get_data(flod_name, case_name):
    """
        存在乱码问题
       :param flod_name: 文件名称
       :param case_name: case名称,匹配yaml文件中的接口(cese)信息
       :return: 接口(cese)信息
       """
    try:
        BASE_PATH = r'C:\Users\Mageline\PycharmProjects\mgl_test\date\test_date'
        filepath = os.path.join(BASE_PATH, 'test_data', flod_name + '.yml')
        with open(filepath, 'r', encoding='gbk', errors='ignore') as f:
            data = yaml.load(f.read(), Loader=yaml.SafeLoader)
            final_data = data[case_name]
        return final_data
    except Exception as e:
        print(e)


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


def login():
    desired_caps = app_lianjie('com.mageline.agent', '.ui.MainActivity')
    # desired_caps = app_lianjie('com.tencent.mm', '.ui.LauncherUI')
    wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    GSTORE['wd'] = wd
    wd.implicitly_wait(8)
    loginpage = JXS_APP_PaGe.login_page(wd)
    #跳过开平动画
    sleep(1)
    wd.tap([(929, 161)], 100)
    hot_search = wd.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')
    if hot_search:
        #输入账号
        loginpage.shuruzhanghao('15835226899')
        # 输入密码
        loginpage.shurumima('123456')
        #勾选协议
        loginpage.gouxuanxieyi()
        # # 点击登录
        loginpage.dianjidenglu()
        sleep(3)
