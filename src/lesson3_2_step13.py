from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def selectors(self, link):
        self.browser.get(link)
        # заполняем обязательные поля
        self.input1 = self.browser.find_element_by_css_selector(".first_block>.first_class>.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(".first_block>.second_class>.second")
        self.input2.send_keys("Lastlonger")
        self.input3 = self.browser.find_element_by_css_selector(".first_block>.third_class>.third")
        self.input3.send_keys("ivan@mail.ru")
        # Отправляем заполненную форму
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Text in field correct")
        time.sleep(5)

    def test_link_correct(self):
        self.selectors("http://suninjuly.github.io/registration1.html")

    def test_link_error(self):
        self.selectors("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    unittest.main()
