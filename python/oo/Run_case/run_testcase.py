
import sys
sys.path.append(r"/root/.jenkins/workspace/selenium_demo1/python/oo")

import time
import unittest

from test_case.ucloud_login import Login_xx
from Run_case import HTMLTestRunner

if __name__ == '__main__':
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(Login_xx))
    path = '/data'+str(time.strftime('%Y-%m-%d %H_%M_%S'))+'.html'
    file = open(path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='自动化测试报告',description='Ucloud登录')
    runner.run(s)
