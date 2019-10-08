## Параметризация тестов - parametrize

PyTest позволяет запустить один и тот же тест с разными входными параметрами. 
Для этого используется декоратор **@pytest.mark.parametrize()**

```python
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
# или
@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
```
запуск:
```bash
$ pytest -s -v  ./src/lesson3_6_step2.py 
```
в итоге получаем два прохода теста - с одним параметром и вторым. в случае класса - каждый тест 

#### Conftest.py - конфигурация тестов
Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py, 
который должен лежать в директории верхнего уровня проекте с тестами.

выносим фикстуру с запуском браузера в conftest.py, тогда тест:
```
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
```
PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами.
Т.е. в случае различных файлов - расскладываем по директориям.

