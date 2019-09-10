Поиск элементов

Вызываем Developer Tools, в поисковой строке

- ``` #bullet  ``` знак # означает, что мы ищем по id со значением bullet
- ``` h1 ``` поиск по tag
- ``` [id="bullet"] ``` поиск по значению
- ``` [name="bullet-cat"] ``` поиск по name
- ``` [class="jumbotron-heading"] ``` поиск по определенному class, или групее, но в заданной последовательности
- ``` .jumbotron-heading``` поиск по class
- ``` $$("div") ``` число элементов на странице
- ``` "#post2 .title" ``` сложный запрос
- ``` "#post2 > div.title" ``` взять элемент с тегом и классом: "div.title", который находится строго на один уровень иерархии ниже чем элемент "#post2" (это задаёт символ ">")
- ``` div.col-sm-4:nth-child(2) img``` если в дочернем классе ищем второй элемент


материалы по селекторам
- (https://learn.javascript.ru/css-selectors)
- (https://www.w3schools.com/cssref/css_selectors.asp)
- (https://habr.com/ru/company/otus/blog/350368/)
- (https://developer.mozilla.org/ru/docs/Web/CSS/CSS_%D0%A1%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D1%8B)
- (https://htmlacademy.ru/courses/42) целый курс по селекторам
- (https://www.w3schools.com/xml/xpath_syntax.asp) XPath

XPath (XML Path Language)
- если других путей нет (CSS-селекторы: сlass, id или name), то используем XPath
- лучше не использовать селекторы вида ``` //div[1]/div[2]/div[3] ```
- XPath запрос всегда начинается с символа / или //
- Символ / аналогичен символу > в CSS-селекторе, а символ // - пробелу.
- Символ [ ] - это команда фильтрации 
    -- по любому атрибуту ``` //img[@id='bullet'] ``` 
    -- по порядковому номеру ``` //div[@class="row"]/div[2] ```
    -- по полному совпадению текста ``` //p[text()="Lenin cat"] ```
    -- по частичному совпадению ``` //div[contains(@class, "navbar")] ```
    -- булевы операции (and, or, not)  ``` //img[@name='bullet-cat' and @data-type='animal'] ```
- Символ * - команда выбора всех элементов ``` //div/*[@class="jumbotron-heading"] ```
- Поиск по классу в XPath регистрозависим ``` //div/*[@class="Jumbotron-heading"] ```
- Console: ``` $x("//....") ```


