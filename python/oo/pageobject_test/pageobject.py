import sys
sys.path.append(r"/root/.jenkins/workspace/selenium_demo1/python")
import time
import csv
from common_test.selenium_driver import driver_Test

class PageObject_test(object):
    def __init__(self,driver):
        self.driver = driver

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def get_CSV(self,csv_file,line):
        logg.info('获取csv数据')
        file= open(csv_file,'r',encoding='utf-8-sig')
        reader = csv.reader(file)
        for index ,row in enumerate(reader,1):
            if index == line:
                return row
