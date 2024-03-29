# Звіт до роботи
## Тема: _Робота з віртуальними середовищами
### Мета роботи: _Навчитись працювати з віртуальними середовищами та працювати з фреймворками та бібліотеками
---
### Виконання роботи
- Результати виконання завдання
    1. Розробив декілька програм
    1. Отримано наступні результати

```python
import requests
response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)
```

![alt-text](https://github.com/ViktorAYE/Brylinskiy-OOP/blob/main/Laba4_Virtual%20Enviroments/Pictures/Screenshot_2_project.png "1")
```python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', content="Hello, I`m Vityusha xD")
if __name__ == '__main__':
    app.run(debug=True)
```
![alt-text](https://github.com/ViktorAYE/Brylinskiy-OOP/blob/main/Laba4_Virtual%20Enviroments/Pictures/Screenshot_1_flask.png "2")

1. Навчився працювати з віртуальними середовищами:
![alt-text](https://github.com/ViktorAYE/Brylinskiy-OOP/blob/main/Laba4_Virtual%20Enviroments/Pictures/Screenshot_3_libs.png "3")
![alt-text](https://github.com/ViktorAYE/Brylinskiy-OOP/blob/main/Laba4_Virtual%20Enviroments/Pictures/Screenshot_4_env.png "4")

### Висновок: 
В ході викоанння лабораторної роботи я навчився працювати з віртуальними середовищами та працювати з фреймворками та бібліотеками
