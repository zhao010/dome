#common基类
#里面写获取公共驱动driver
#和日志配置
#
import sys
sys.path.append(r"/root/.jenkins/workspace/selenium_demo1/python")
import logging
from logging import config
from selenium import webdriver
#配置文件的路径
#File_config = 'python/oo/config_test/log.conf.py'
#读取配置文件
#config.fileConfig(File_config)
#生成日志文件
#logg = logging.getLogger()

def driver_Test():
    opt = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    opt.set_headless()
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # 用的是谷歌浏览器
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=opt)
    print('运行成功')
    return driver
