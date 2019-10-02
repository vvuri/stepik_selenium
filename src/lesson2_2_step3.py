from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")
    num3 = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(num3))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()