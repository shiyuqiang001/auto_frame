import unittest
from BeautifulReport import BeautifulReport as bf
from Auto_Ui.test.case.ui.test_baidu import TestBaiDu
from Auto_Ui.utils.mail import Email
from Auto_Ui.utils.config import REPORT_PATH, Config
from Auto_Ui.utils.generator import random_name

class TestRun(unittest.TestCase):

    suite = unittest.TestSuite()  # 定义一个测试集合
    suite.addTest(unittest.makeSuite(TestBaiDu))  # 把写的用例加进来（将TestClass类）加进来
    run = bf(suite)  # 实例化BeautifulReport模块

    run.report(filename='G3项目', description='百度搜索')

    emil = Config().get('mail')
    report = REPORT_PATH + '\G3项目.html'
    # e = Email(title=emil.get('title'),
    #           message=emil.get('message'),
    #           receiver=emil.get('receiver'),
    #           server=emil.get('server'),
    #           sender=emil.get('sender'),
    #           password=emil.get('password'),
    #           path=report
    #           )
    #
    # e.send()
    print(random_name())
