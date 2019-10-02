## Testing in Python - assert

Инструкция **assert** выдает True или False
```python
>>> assert abs(-42) == 42
```
в сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту.
```python
assert self.is_element_present('create_class_button', timeout=30), "No create class button"
```

#### Форматирование строк 
с помощью str.format
```python
"Let's count together! {}, then goes {}, and then {}".format("one", "two", "three")
```
с помощью f-strings:
```python
str1 = "one"
str2 = "two"
str3 = "third"
f"Let's count together! {str1}, then goes {str2}, and then {str3}"

actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"

f"{2+3}"   # выдаст '5'
```
Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст на странице может измениться.

#### Строки
Поиск **подстроки** в строке **in** or **find**
```
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

assert 'Name' in s, "вхождение подстроки в строку"
```
Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку или -1.



