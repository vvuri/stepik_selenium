## Маркировка тестов - mark

Выделение в тестах smoke, regression и т.д. 
В PyTest используется маркировка тестов или метки (marks)
**@pytest.mark.mark_name**, где mark_name - произвольная строка.
Для запуска используем **-m** smoke - например
```bash
$ pytest -s -v -m mark_name test_fixture8.py
```

В последних версиях PyTest настоятельно рекомендуется регистрировать метки явно перед использованием
Создайте файл **pytest.ini** в корневой директории вашего тестового проекта и добавьте в файл следующие строки:
```ini
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
```    
Текст после знака ":" является поясняющим - его можно не писать.
Так же можно маркировать целый тестовый класс. В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.

**Инверсия** - не запускать данные тесты **-m "not smoke"**
```bash
$ pytest -s -v -m "not smoke" test_fixture8.py
```

**Объединение тестов с разными маркировками** Запустит smoke и regression-тесты:
```bash
pytest -s -v -m "smoke or regression" test_fixture8.py
```

**Выбор тестов, имеющих несколько маркировок**
```bash
pytest -s -v -m "smoke and win10" ./src/test_3_5_step3.py
```
**Пропуск тестов** - **@pytest.mark.skip**

**XFail**: помечать тест как ожидаемо падающий - **@pytest.mark.xfail**
в прогоне вместо **PASS** он будет **XFAIL** - если он пройдет, то станет **XPASS** (“unexpectedly passing” - неожиданно проходит)
можно добавить дополнительное сообщение reason @pytest.mark.xfail(reason="fixing this bug right now")
и при запуске с ключем pytest -rx будет дополнительное сообщение
[Дополнительные трюки](https://docs.pytest.org/en/latest/skipping.html)



