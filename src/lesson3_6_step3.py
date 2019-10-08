import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
import math

def get_answer():
    return str(math.log(int(time.time())))

def get_url(num):
    return "https://stepik.org/lesson/"+num+"/step/1"

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898","236899", "236903","236904", "236905"])
def test_exception1(url):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(get_url(url))
        
        input = browser.find_element_by_css_selector(".ember-text-area.ember-view")
        input.send_keys(get_answer())

        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        correct = browser.find_element_by_css_selector(".smart-hints__hint")
        #print(">>"+ correct.text)
        assert correct.text == "Correct!"
    finally: 
        #time.sleep(15)
        browser.quit()
