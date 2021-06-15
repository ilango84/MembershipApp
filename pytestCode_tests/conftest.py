import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/ilangovanponnuraman/Downloads/chromedriver-2")
    elif browser_name == "FireFox":
        pass
        # print('firefoxx driver path here')
    elif browser_name == "IE":
        pass
        # print('IE driver path here')
    elif browser_name == "safari":
        pass
        # print('Safari driver path here')

    driver.get('https://qa-member.astm.org/MyASTM')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

