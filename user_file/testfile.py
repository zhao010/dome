import time
#coding = utf-8
from selenium import webdriver

        # 创建chrome参数对象
opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.set_headless()
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
        # 用的是谷歌浏览器
driver = webdriver.Chrome('/usr/bin/chromedriver',options=opt)
from selenium.webdriver.common.by import By

# connect = pymysql.connect(host='127.0.0.1',port=3306,db='pysql',user='root',password='mhxzkhl',charset='utf8')
#
list = []

driver = webdriver.Chrome('/usr/bin/chromedriver',options=opt)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://console.ucloud.cn/uhost/uhost/create')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'input[id="username"]').send_keys('17600570787@163.com')
driver.find_element(By.CSS_SELECTOR,'input[id="password"]').send_keys('PGTuxw@042')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]//div[2]/button').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[1]/a/button').click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'div[class="qm__info u-clearfix"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'li[class="J_MenuItem qm__list"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'a[class="u-blue"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'div[class="uc-select__selected-value"]').click()
region_list = driver.find_elements(By.CSS_SELECTOR,'span[class*="region-name"]')
try:

    for region in region_list:
        if region.text == list[0]:
            region.click()
except:
    print('hah')
time.sleep(4)

Peizhi_list = driver.find_elements(By.CSS_SELECTOR,'span[class="config-header"]')
try:
    for Peizhi in Peizhi_list:
        if Peizhi.text == '自定义配置':
            Peizhi.click()
except:
    print('hh')
button1_list = driver.find_elements(By.CSS_SELECTOR,'button[class*="uc-fe-button uc-fe-button-size-lg"]')
try:
    for button1 in button1_list:
        if button1.text == list[1]:
            button1.click()
except:
    print('button 选择有报错')
button2_list = driver.find_elements(By.CSS_SELECTOR,'button[class*="uc-fe-button uc-fe-button-size-lg"]')
try:
    for button2 in button1_list:
        if button2.text == list[2]:
            button2.click()
except:
    print('button 选择有报错')
button3_list = driver.find_elements(By.CSS_SELECTOR,'button[class*="uc-fe-button uc-fe-button-size-lg"]')
try:
    for button3 in button1_list:
        if button3.text == list[3]:
            button3.click()
except:
    print('button3 选择有报错')
button4_list = driver.find_elements(By.CSS_SELECTOR,'button[class*="uc-fe-button uc-fe-button-size-lg"]')
try:
    for button4 in button1_list:
        if button4.text == list[4]:
            button4.click()
except:
    print('button3 选择有报错')
driver.find_element(By.CSS_SELECTOR,'i[class="uc-fe-icon icon__cross css-16jq2tw-IconWrap-IconWrap ep7ivy70"]').click()
def set_scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
set_scroll_into_view(element=driver.find_element(By.CSS_SELECTOR, 'div[class="uc-fe-card u-mt12 css-mk9nbh-CardWrap-CardWrap ekqfw646"]'))

Peizhi2_list = driver.find_elements(By.CSS_SELECTOR,'span[class="config-header"]')
try:
    for Peizhi2 in Peizhi_list:
        if Peizhi2.text == '自定义网络':
            Peizhi2.click()
except:
    print('hh')

def set_scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
set_scroll_into_view(element=driver.find_element(By.CSS_SELECTOR, 'svg[class="uc-fe-checkbox-icon css-12dxizz-SvgIconWrapper-inlineBlockWithVerticalMixin-SvgIconWrapper e1diw3at0"]'))

driver.find_element(By.CSS_SELECTOR,'svg[class="uc-fe-checkbox-icon css-12dxizz-SvgIconWrapper-inlineBlockWithVerticalMixin-SvgIconWrapper e1diw3at0"]').click()

def set_scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
set_scroll_into_view(element=driver.find_element(By.CSS_SELECTOR, 'div[class="chargeinfov4-wrapper"]'))

momey = (driver.find_elements(By.CSS_SELECTOR,'div[class="uc-fe-col u-tr css-gudzge-ColWrap-ColWrap e1a3ygz30"]')[1].text)
print(momey)
print('**************************************8')
driver.quit()
# list.append(momey)
# print(list)

# cursor = connect.cursor()
# addsql = "insert into offering(region,Big_type,Small_typr,Cpu_type,Storage_typr,Money)  values('%s','%s','%s','%s','%s','%s')"%(str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5]))
# cursor.execute(addsql)
# connect.commit()
# cursor.close()
# connect.close()


