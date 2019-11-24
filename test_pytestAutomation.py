import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

#chrome_path = r'/usr/local/bin/chromedriver'
#firefox_path = r'/usr/local/bin/geckodriver'

#Fixture for google automation
#Testing for GUI automation
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
 
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("http://localhost:8000/projects/")
            print(self.driver.title)
            sleep(5)



    
