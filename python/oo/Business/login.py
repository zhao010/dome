from selenium.webdriver.common.by import By

from pageobject_test.pageobject import PageObject_test



class Login(PageObject_test):

    username = (By.CSS_SELECTOR, 'input[placeholder="登录邮箱"]')
    password = (By.CSS_SELECTOR, 'input[id="password"]')
    login_button = (By.XPATH, '//*[@id="app"]/div/div[2]//div[2]/button')

    def denglu(self,username,password):
        self.driver.get('https://passport.ucloud.cn/login?service=https%3A%2F%2Fconsole.ucloud.cn%2F#login')
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
