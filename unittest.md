## unittest

- Название тестового метода должно начинаться со слова "test_" или заканчиваться словом "_test".
- Тесты обязательно должны находиться в специальном тестовом классе
- Вместо assert должны использоваться специальные assertion методы

```python
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
```

[Документация](https://docs.python.org/3/library/unittest.html)


