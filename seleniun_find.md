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

####Click
Checkbox (чекбокс или флажок) 
``` <input type="checkbox"> ```
Radiobutton (радиобаттон или переключатель)
```html 
<input type="radio" name="language" value="python" checked>
<input type="radio" name="language" value="selenium">
или 
<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
```
код нажатия
```python
option1 = browser.find_element_by_css_selector("[value='python']")
или
option1 = browser.find_element_by_css_selector("[for='python']")

option1.click()
```

#### Метод get_attribute
```
<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>
```
```python
people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")

print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
```
 все методы WebDriver взаимодействуют с браузером с помощью JavaScript => true с маленькой буквы
```python
assert people_checked == "true", "People radio is not selected by default"
``` 
Если атрибута нет, то метод get_attribute вернёт значение None. 
```python
assert robots_checked is None
```

#### Выпадающие списки
```html
<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
 <option selected>--</option>
 <option value="1">Python</option>
 <option value="2">Java</option>
 <option value="3">JavaScript</option>
</select>
```
```python
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
or
browser.find_element_by_css_selector("[value='1']").click()
```

Более удобный способ - использование класса Select из библиотеки WebDriver:
```python
from selenium.webdriver.support.ui import Select

select = Select(browser.find_element_by_tag_name("select"))

select.select_by_value("1") # ищем элемент с текстом "Python"
or
select.select_by_visible_text("Python")  # ищем элемент по видимому тексту
or
select.select_by_index(1) #ищем элемент по его индексу или порядковому номеру
```

#### Завершение работы:
**browser.close()** закрывает текущее окно браузера
**browser.quit()** закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.
И расположить в разделе **finally**


#### Выполнение JavaScript 
Прежде чем использовать данный скрипт в тестах, вы можете проверить, как он работает прямо в браузере, выполнив код в консоли браузера. 
Затем можете добавить его в ваш автотест с помощью execute_script(javascript_code)
```python
browser.execute_script("alert('Robots at work');")

browser.execute_script('document.title="Script executing";')

browser.execute_script("alert(\"Robots at work\");")  # внутреннее экранирование
```

Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
```JavaScript
element = browser.execute_script('document.getElementsByName("name")')
```
Так же есть конструкции:
- getElementById
- getElementsByTagName
- getElementsByClassName
- querySelector - для CSS
- querySelectorAll - для CSS (находит все совпадения)
- evaluate - для XPATH.
