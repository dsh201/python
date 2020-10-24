#LISTS
# m append дополняет список элементами
# list_ = []
# list_.append('world')
# print(list_)
# print(len(list_))
# list_.append('hello')
# print(list_)
# print(len(list_))











# range создание списков каких-либо чисел
# list_ = list(range(1, 50, 2))
# print(list_)

# insert получает два аргумента, первый индекс, второй сам элемент
# cars = ['Mersedes', 'Subaru', 'Honda']
# print(len(cars))
# cars.insert(len(cars), 'Toyota')
# print(cars)
# cars.insert(0, 23)
# print(cars)
# list_ = list(range(1, 5))
# cars.insert(2, list_)
# print(cars)
# print(len(cars))

# m remove удаляет элементы по названию
# laptops = ['Lenovo', 'Asus', 'HP', 'HP']
# print('before remove', laptops)
# laptops.remove('HP')
# print('after remove', laptops)

# m pop удаляет и возвращает элемент/ по умолчанию последний
# programming = ['c', 'python', 'js', 'go', 'java']
# print('before', programming)
# last_element = programming.pop(1)
# print('after', programming)
# print(last_element)

# method index возвращает индекс элементами
# movies = ['звездные воины', 'gentelmans', 'why him', 'godfather', '1+1']
# print(movies.index('1+1'))
# number_in_list = movies.index('1+1')
# print(number_in_list)
# print(number_in_list ** number_in_list)
# print(type(number_in_list))

# method count считатет колво элементов
# list_ = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']
# print(list_.count('apple'))
# string = 'hello world'
# print(string.count('l'))
# new_list = list(string)
# print(new_list)

# method reverse разворачивает список в обратную сторону
# list_ = [1,2,3,4,5,6,7,8,9,0]
# print(list_)
# list_.reverse()
# print(list_)

# method sort сортирует элементы в списке по ключу
# numbers = [2, 1, 3, 5, 4]
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# method copy копирует список
# list_ = ['apple', 'banana', 'pineapple', 'strawberry', 'apple']
# new_list = list_.copy()
# print(new_list)
# print(list_)
#
# new_list.append('blackberry')
# print(new_list)

#method extend расширяет список другим списком(складывает)
# nums = [1,2,3]
# nums2 = [4,5,6]
# # nums = nums + nums2
# # print(nums)
# # nums.extend(nums)
# nums += nums2
# print(nums)

# method clear очищает список
# nums = [1, 2, 3, 4, 5, 6, 7]
# # print(nums)
# # nums.clear()
# # print(nums)
# print(nums[::-1])

# tuple
# 24.10.2020 Словари

# dict_with_pairs = {'Ключ1': 'Значение', 'Ключ2': 'Значение2'}

# m fromkeys создает новый словарь из переданных ему ключей
# names = {'name': 'Diana', 'name2': 'Tim' }
# print(names['name'])
#
#
# dictionary = dict.fromkeys(['key1', 'key2'])
# print(dictionary)

# извлечение данных из словаря
# test = {'name': 'Jonh', 'lastname': 'Snow'}
# print(test['name'])
# print(test['lastname'])

# dictionary




# method get получает по ключу значение
# cars = {'mersedes', '221', 'bmv', '7501', 'subaru', 'impreza'}
# print(cars.get('subaru'))
# print(cars['subaru'])

# m keys выводит все ключи

# m values выводит все значения

# m pop удаляет по ключу и возвращает значение нужно указывать ключ
# dict_ = {'first': '1st', 'second': '2nd'}
# print(dict_)
# first = dict_.pop('first')
# print(dict_)
# print(first)

# m popitem вырезает последнюю пару: ключ и значение
# cars = {'mersedes': '221', 'bmv': '7501', 'subaru': 'impreza'}
# deleted = cars.popitem()
# print(cars)
# m update
# laptops = {'lenovo': 'yoga', 'macbook': 'pro', 'asus': 'zepfyrus'}
# laptops2 = {'dell': 'allienware'}
# print(laptops)
# laptops.update(laptops2)
# print(laptops)

# m setdefault сохраняет значение по ключу
# dict_ = {'key1': 1, 'key2': 2, 'key3': 3}
# new_dict = dict_.setdefault('key2')
# print(new_dict)
# new = dict_['key2']
# print(new)
# new2 = dict_.get('key2')
#
#Другие способы создания словарей
# capitals = dict(Russia = 'Moscow', Kyrgizstan = 'Bishkek', USA = 'Washington')
# print(capitals)

# capitals = dict([('Russia', 'Moscow')])
# print(capitals)

# Множество\set - содержит в себе множество уникальных значений.



# m add добавляет элемент в множество
# set_ = {1, 2, 3}
# print(set_)
# print(type(set_))
# set_.add(4)
# print(set_)

# m remove удаляет элемент из множества
# set_ = {2,3,4,5,6,7,1,8,9}

# m discard также удаляет, как и remove
# set_ = {2,3,4,5,6,7,1,8,9}
# set_.discard(1)
# print(set_)

# m pop вырезает элемент
# set_ = {1,2,3,4,5,6,7,8,9,0}
# print(set_)
# print(set_.pop())





