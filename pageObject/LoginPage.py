from selenium.webdriver.common.by import By


class LoginPage:
    userName = (By.CSS_SELECTOR, "input[name='userName']")
    passWord = (By.NAME, "password")
    submitBtn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver


    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def getPassWord(self):
        return self.driver.find_element(*LoginPage.passWord)

    def submitButton(self):
        return self.driver.find_element(*LoginPage.submitBtn)

