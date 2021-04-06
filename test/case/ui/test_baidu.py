import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Auto_Ui.utils.config import Config,DATA_PATH,DRIVER_PATH
from Auto_Ui.utils.file_reader import ExcelReader
from Auto_Ui.utils.log import logger
from BeautifulReport import BeautifulReport as bf
from Auto_Ui.test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xls'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='firefox').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        '''百度搜索'''
        datas = ExcelReader(self.excel).data
        for d in datas:
            logger.debug(d)
            with self.subTest(data=d):
                print(d['search'])
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    print(link.text)
                    logger.info(link.text)
                self.sub_tearDown()



# class TestBaiDu(unittest.TestCase):
#     URL = Config().get('URL')
#     excel = DATA_PATH + '/baidu.xls'
#
#     locator_kw = (By.ID, 'kw')
#     locator_su = (By.ID, 'su')
#     locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
#
#     def sub_setUp(self):
#         self.driver = webdriver.Firefox(executable_path=DRIVER_PATH + '\geckodriver.exe')
#         self.driver.get(self.URL)
#
#     def sub_tearDown(self):
#         self.driver.quit()
#
#     def test_search(self):
#         datas = ExcelReader(self.excel).data
#         for d in datas:
#             with self.subTest(data=d):
#                 self.sub_setUp()
#
#                 self.driver.find_element(*self.locator_kw).send_keys(d['search'])
#                 self.driver.find_element(*self.locator_su).click()
#                 time.sleep(2)
#                 links = self.driver.find_elements(*self.locator_result)
#                 for link in links:
#                     logger.info(link.text)
#                 self.sub_tearDown()




if __name__ == '__main__':
    suite = unittest.TestSuite()  # 定义一个测试集合
    suite.addTest(unittest.makeSuite(TestBaiDu))  # 把写的用例加进来（将TestCalc类）加进来
    run = bf(suite)  # 实例化BeautifulReport模块
    run.report(filename='test', description='百度搜索')


