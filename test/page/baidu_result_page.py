from selenium.webdriver.common.by import By
from Auto_Ui.test.page.baidu_main_page import BaiDuMainPage
from Auto_Ui.test.common.browser import Browser

class BaiDuResultPage(BaiDuMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        self.refresh()##刷新一下
        return self.find_elements(*self.loc_result_links)
