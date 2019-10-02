s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

assert 'Name' in s, "вхождение подстроки в строку"

assert 'Name1' in s, "вхождение подстроки в строку"