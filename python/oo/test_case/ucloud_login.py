
import sys
sys.path.append(r"/root/.jenkins/workspace/selenium_demo1/python/oo")
from Business.login import Login
#from common_test.selenium_driver import logg
from common_test.unit_test import Myuint_test



class Login_xx(Myuint_test):
    fliepath = '/Users/didi/Desktop/python/oo/data/user.csv'
    def test1(self):
        L = Login(self.driver)
        row = L.get_CSV(csv_file=self.fliepath,line=1)
        L.denglu(row[0],row[1])
    def test2(self):
        L = Login(self.driver)
        row = L.get_CSV(csv_file=self.fliepath,line=2)
        L.denglu(row[0],row[1])
