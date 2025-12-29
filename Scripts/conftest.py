import time
import pytest

from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

## setup --> driver = webdriver.Chrome()
