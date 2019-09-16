from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")
# or 
# button = browser.find_element(By.ID, "submit_button")

print(button)
# DevTools listening on ws://127.0.0.1:62897/devtools/browser/e186aead-9d1b-4f34-b348-edf4eccaa002
# <selenium.webdriver.remote.webelement.WebElement (session="bc05b95f3149ee9b04428725cef98651", element="abbd2eeb-755d-4a5f-a7ff-6d94176361f8")>