from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # alert window
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    x_answer = browser.find_element_by_css_selector("#answer")
    x_answer.send_keys(calc(x))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()