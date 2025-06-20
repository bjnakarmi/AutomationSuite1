from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    print("Setting up the browser ...")
    options = webdriver.ChromeOptions()
    options.add_argument('--Headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    print("Tearing down the browser ...")
    driver.quit()


