## Stepic Python QA course

1. Install Python 3
```bash
$ python --version
Python 3.7.4
```

2. Создадим виртуальное окружение с помощью команды python3
```bash
$ python -m venv selenium_env
```

3. Активируем окружение:
```bash
$ source selenium_env/Scripts/activate
(selenium_env)
```
Выход из виртуального окружения командой: deactivate  - но сработал с удалением пактеов???

4. Test
```python
$ python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, Selenium!")
Hello, Selenium!
```

5. Install Selenium
```bash
$ pip install selenium==3.14.0

$ pip list | grep selenium
selenium   3.14.0 
```

6. Драйвер
https://sites.google.com/a/chromium.org/chromedriver/downloads
смотрим на версию браузера
Версия 76.0.3809.132 (Официальная сборка), (64 бит)
- качаем поддерживаемый драйвер
- закидываем в C:/soft
- прописываем путь в PATH
- перезапустить консоль
```bash
$ chromedriver
Starting ChromeDriver 76.0.3809.126
```
Для MacOS
```bash
$ brew install wget
$ cd ~/Downloads
$ wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip
$ unzip chromedriver_mac64.zip
$ sudo mv chromedriver /usr/local/bin
$ chromedriver --version
```

7. Firefox и Selenium
[geckodriver](https://github.com/mozilla/geckodriver/releases) 
распакуйте его в папку C:\soft\ на Windows + PATH прописать, /usr/local/bin на Ubuntu и macOS

8. Плагин перезапуска упавших тестов
```
$ pip install pytest-rerunfailures==7.0
```

**Полезные ссылки:**
- [Документация Selenium with Python](https://selenium-python.readthedocs.io/)
- [WebDriver for Chrome](http://chromedriver.chromium.org/getting-started)
- [Explicit Waits](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)

- [Python online](https://repl.it/repls/KnobbyFastFields)
- [PyTest Eng](https://realpython.com/python-testing/)

- [GIT Интерактивное обучение](https://learngitbranching.js.org/)
- [GIT-документация Rus](https://git-scm.com/book/ru/v2/)
- [GIT альтернативное описание](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html)
- [GIT по шагам](https://githowto.com/ru/)

Сохраняем все версии пакетов в специальный файл requirements.txt.
```bash
pip freeze > requirements.txt
```
в свежем окружении для развертывания
```bash
pip install -r requirements.txt
```