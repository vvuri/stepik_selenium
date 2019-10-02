from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ищем элемент 
    price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element_by_css_selector("button#book")
    button.click()

    # появление дополнительного блока
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    x_answer = browser.find_element_by_css_selector("#answer")
    x_answer.send_keys(calc(x))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()