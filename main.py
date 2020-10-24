# name = 'diana'
# age = 23
# print(name + " " + str(age))
# # Home work
# # Ex 1
# a = 2
# b = 7
# print(a, b, sep = ';')
# print(a - b)
# print(a, '-', b, '=', a - b)
# # Ex 2
# c = 36
# d = 5
# print(c % d)
# print(c, '%', d, '=', c % d)

# Class work 22/10/2020
# method split делит строку по разделителю на отдельные слова
# text = 'hello,world,good,day'
# print(text.split(','))

# method isdigit проверяет все ли символы в строке цифры\ возвращает ложь или истину
# num = input('Введите число: ')
# print(num.isdigit())

# method isalpha проверяет являются ли символы в строке буквами
# text = input('Input here: ')
# print(text.isalpha())

# method isalnum проверяет все ли символы в строке цифры и буквы
# text = input('Input: ')
# print(text.isalnum())

# method replace заменяет часть строки
# string = 'Hello world'
# print(string.replace('Hello', 'Goodbye'))
# print(string.replace('o', '*', 2))

# m-d isupper все ли символы в верхнем регистре
# text = input('Input: ')
# print(text.isupper())

# m-d islower проверяет все ли символы в нижнем регистре
# text = input('Input: ')
# print(text.islower())

# method isspace проверяет все ли символы пробелы, табы либо переводы строки
# text = '\n'
# print(text.isspace())

# method istitle проверяет, является ли строка заголовком
# text1 = 'hello world'
# text2 = 'Hello World'
# print(text1.istitle())
# print(text2.istitle())

# Методы преобразования строк
# method lower перевод букв в нижний регистр
# text = 'Hello WORLD'
# text2 = text.lower()
# print(text2)
# print(text)

# method upper переводит буквы в верхний регистр
# string = 'Hello world'
# print(string.upper())

# method startswith проверяет начинается ли строка с определенных символов
# text = 'Hello world'
# print(text.startswith('H'))

# method endwith проверяет заканчивается ли строка на какие - либо символы (напр. проверка написания адреса э. п.)
# mail = 'example@google.com'
# print(mail.endswith('m'))

# method join склеивает строку, собирает по кусочкам из разных частей
# text = 'hello, my name is Diana'
# text_splited = text.split()
# print(text_splited)
# text2 = '_'.join(text_splited)
# print(text2)

# method ord выводит номер символа из таблицы ASCII
# print(ord('w'))

# method count считает количество символов переданных в скобках
# text = 'Hello World'
# print(text.count('l'))

# method strip, lstrip, rstrip удаляет пробелы в начале и конце строки
# text = '   hello world   '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# method swapcase меняет регистр на противоположный
# text = 'Hello world'
# text2 = 'hELLO WORLD'
# print()

# Срез строки
# text = 'Hello world'
# print(text[0:5:2])
# print(text[::-1])

# text = input('Input text: ')
# print(text[5:0:-2])
# if text == text[::-1]:
#     print('Текст читается одинаково')
# else:
#     print('Текст не читается одинаково')

# Форматирование строк
#  name = input('Введите свое имя: ')
#  age = input('Введите свой возраст: ')
#  print('Вас зовут ' + name + '. Ваш возраст ' + age)
#  print(f"Вас зовут {name}. Ваш возраст {age}.") - форматирование строк
# print("Hello, %s" % name) - старый способ форматирования. !ныне не используется!
# print("Hello" {}.format(name)) - тоже старый способ
#  text = """В языке Питон нет отдельного символьного типа. Символ — это просто строка длины 1.Строка считывается со стандартного вво
# да функцией input().Для двух строк определена операция сложения (конкатенации), также определена операция умножения стр
# оки на число.
# """
# print(text)
# text = 'hello \t world'
# print(text)
