Stepic Python QA course

1. Install Python 3
```
$ python --version
Python 3.7.4
```

2. Создадим виртуальное окружение с помощью команды python3
```
$ python -m venv selenium_env
```

3. Активируем окружение:
```
$ source selenium_env/Scripts/activate
(selenium_env)
```
Выход из виртуального окружения командой: deactivate  - но сработал с удалением пактеов???

4. Test
```
$ python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, Selenium!")
Hello, Selenium!
```

5. Install Selenium
```
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
```
$ chromedriver
Starting ChromeDriver 76.0.3809.126
```
Для MacOS
```
$ brew install wget
$ cd ~/Downloads
$ wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip
$ unzip chromedriver_mac64.zip
$ sudo mv chromedriver /usr/local/bin
$ chromedriver --version
```


PS
Python online https://repl.it/repls/KnobbyFastFields