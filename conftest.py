import pytest
from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=opts)

    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.maximize_window()

    yield driver

    driver.quit()