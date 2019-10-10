## Firefox и Selenium-драйвера geckodriver

Selenium-драйвер для Firefox носит название geckodriver. 
Скачайте последнюю версию geckodriver с [сайта](https://github.com/mozilla/geckodriver/releases) и распакуйте его в папку C:\geckodriver на Windows, /usr/local/bin на Ubuntu и macOS.
В итоге положил geckodriver в C:\soft\ + прописал в PATH

```bash
$ python ./src/lesson3_6_step5.py 

$ pytest -s -v --browser_name=firefox test_cmd.py
```
Отличия в коде 
```python
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")
```
