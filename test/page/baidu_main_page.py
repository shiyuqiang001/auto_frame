from time import sleep
from selenium.webdriver.common.by import By
from Auto_Ui.test.common.page import Page


class BaiDuMainPage(Page):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')

    def search(self, kw):
        """搜索功能"""
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()
        sleep(3)
        self.save_screen_shot()
        self.refresh()
