from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get()
driver.find_element(By.CSS_SELECTOR,"")
driver.find_element()
elements_list = driver.find_elements(By.CSS_SELECTOR,"")
for element in elements_list:
    if element.text == 'xixi':
        element.click()