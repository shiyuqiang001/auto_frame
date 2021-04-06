from Auto_Ui.test.common.browser import Browser


class Page(Browser):
    # 更多的封装请自己动手...
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    ##获得操作浏览器的driver，通过父类
    def get_driver(self):
        return self.driver

    # 查询元素
    #定位语句不唯一，能够查到多个函数的话，默认值返回页面中出现的第一个
    def find_element(self, *args):
        return self.driver.find_element(*args)

    #查询元素
    ##定位语句不唯一，能够查到多个函数的话，返回一个列表
    def find_elements(self, *args):
        return self.driver.find_elements(*args)
