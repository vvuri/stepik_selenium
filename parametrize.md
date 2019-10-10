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

#### передача параметров в командной строке
Это делается с помощью встроенной функции pytest_addoption и фикстуры request.
[подробнее](https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption)
Запуск тестов будет возможен только с параметрами, без них ошибка.
или задать значения по-умолчанию
```
parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
```
Пример в ./src/section_params/test_parser.py
```bash
$  pytest -s -v ./src/section_params/test_parser.py
$ pytest -s -v --browser_name=firefox ./src/section_params/test_parser.py
```

#### Плагины 
[Плагины-расширения pytest](https://docs.pytest.org/en/latest/plugins.html)
 
#### перезапуск тестов - pytest-rerunfailures
 **Flaky-тесты** или "**мигающие**" авто-тесты, т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов, могут иногда падать, хотя всё остальное время они проходят успешно.
```bash
$ pip install pytest-rerunfailures==7.0
```

```bash
$ pytest -v --tb=line --reruns 1 --browser_name=chrome ./src/section_params/test_rerun.py
```
где
"--reruns n", где n - это количество перезапусков
"--tb=line", чтобы сократить лог с результатами теста

#### Запуск автотестов для разных языков интерфейса
Язык передается в Headers (заголовке запроса) параметр {accept-language: ru, en} - вначале попробует русский, иначе следующий.
Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)
```
Для Firefox объявление нужного языка будет выглядеть немного иначе:
```python
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
```
