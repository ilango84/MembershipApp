import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.LoginPage import LoginPage
from testData import LoginPageData
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):

    def test_LoginPage(self, getData):
        loginPage = LoginPage(self.driver)
        #time.sleep(6)

        self.verifyElementPresence("userName", 6)
        loginPage.getUserName().send_keys(getData["username"])
        loginPage.getPassWord().send_keys(getData["password"])
        loginPage.submitButton().click()



        #self.driver.refresh()

    @pytest.fixture(params=LoginPageData.LoginPageData.test_LoginPage_data)
    def getData(self, request):
        return request.param
