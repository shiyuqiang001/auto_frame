import time
import os
from selenium import webdriver
from Auto_Ui.utils.config import DRIVER_PATH, REPORT_PATH

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
FIREFOX_PATH =  DRIVER_PATH + '\geckodriver.exe'
##'firefox': 'wires'
TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': FIREFOX_PATH, 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    ##初始化webdriver
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None
    ##访问
    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self
    ##截屏
    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot
    ##关闭浏览器
    def close(self):
        self.driver.close()
    ##退出浏览器
    def quit(self):
        self.driver.quit()
    ##浏览器后退
    def back(self):
        self.driver.back()
    ##浏览器前进
    def forward(self):
        self.driver.forward()
    ##刷新浏览器
    def refresh(self):
        self.driver.refresh()