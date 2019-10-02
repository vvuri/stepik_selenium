from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('[name="firstname"]')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_tag_name('[name="lastname"]')
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_tag_name('[name="email"]')
    input3.send_keys("ivan@stepik.org")

    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'zero.txt')
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()