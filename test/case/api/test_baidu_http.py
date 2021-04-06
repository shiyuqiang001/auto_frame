import unittest
from Auto_Ui.utils.config import Config, REPORT_PATH
from Auto_Ui.utils.client import HTTPClient
from Auto_Ui.utils.log import logger
from BeautifulReport import BeautifulReport as bf
from Auto_Ui.utils.assertion import assertHTTPCode, assertHTTPAssertIn
from Auto_Ui.utils.extractor import  JMESPathExtractor

class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('api')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')
        self.j = JMESPathExtractor()
    def test_baidu_http1(self):
        res = self.client.send()
        j_1 = self.j.extract(query='data.forecast[1].date', body=res.text)
        j_2 = self.j.extract(query='data.ganmao', body=res.text)
        print(j_1)
        print(j_2)
        print("执行成功")
        logger.debug(res.text)
        #self.assertIn('百度一下，你就知道', res.text)

    def test_baidu_http2(self):
        res = self.client.send()
        assertHTTPCode(res)
        print("执行成功")
        logger.debug(res.text)



if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()  # 定义一个测试集合
    suite.addTest(unittest.makeSuite(TestBaiDuHTTP))  # 把写的用例加进来（将TestClass类）加进来
    run = bf(suite)  # 实例化BeautifulReport模块

    run.report(filename='G2项目', description='百度')
