##Selenium

```bash
$ pip install selenium
```

Cуществуют следующие методы поиска элементов:
- **find_element_by_id** - поиск по уникальному атрибуту id элемента - наиболее стабильный;
- **find_element_by_css_selector** - поиск элемента с помощью правил на основе CSS - самый универсальный метод поиска;
- **find_element_by_xpath** - поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
- **find_element_by_name** - поиск по атрибуту name элемента;
- **find_element_by_tag_name** - поиск элемента по названию тега элемента;
- **find_element_by_class_name** - поиск по значению атрибута class;
- **find_element_by_link_text** - поиск ссылки на странице по полному совпадению;
- **find_element_by_partial_link_text** - поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit")
or
button = browser.find_element(By.ID, "submit_button")
```

Поля класса By, которые можно использовать для поиска find_element:
- **By.ID** – поиск по уникальному атрибуту id элемента;
- **By.CSS_SELECTOR** – поиск элементов с помощью правил на основе CSS;
- **By.XPATH** – поиск элементов с помощью языка запросов XPath;
- **By.NAME** – поиск по атрибуту name элемента;
- **By.TAG_NAME** – поиск по названию тега;
- **By.CLASS_NAME** – поиск по атрибуту class элемента;
- **By.LINK_TEXT** – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
- **By.PARTIAL_LINK_TEXT** – поиск ссылки по частичному совпадению текста.
Важно - возвращается только первый найденный элемент.

Если find_element не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException.

**find_elements_by** - содержит все те же методы поиск
Если find_elements не смог найти элемент на странице, то он вернёт пустой список.



#### Завершение работы:
**browser.close()** закрывает текущее окно браузера
**browser.quit()** закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.
И расположить в разделе **finally**


