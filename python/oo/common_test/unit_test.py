
#创建unittest框架，
#
#


import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest

from common_test.selenium_driver import driver_Test, logg


class Myuint_test(unittest.TestCase):
    def setUp(self):
        logg.info('_________获取驱动__________')
        self.driver = driver_Test()
    def tearDown(self):
        logg.info('_________关闭浏览器__________')
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
