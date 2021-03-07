from selenium import webdriver
from chromedriver_py import binary_path
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=binary_path)
    yield driver
    driver.quit()

