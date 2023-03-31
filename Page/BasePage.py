# page基类
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy



class Page(object):
    """
        Page基类，所有页面page都应该继承该类
    """

    def __init__(self, wd):
        self.wd = wd

    def find_element(self, *loc):
        print(*loc)
        return self.wd.find_element(*loc)

    def find_elements(self, *loc):
        print(*loc)
        return self.wd.find_elements(*loc)

    def text(self, *loc):
        return self.find_element(*loc).text

    def get_attribute(self, attribute, loc):
        return self.find_element(*loc).get_attribute(attribute)

    def click(self, loc):
        self.find_element(*loc).click()

    def sendkeys(self, loc, text):
        self.find_element(*loc).send_keys(text)