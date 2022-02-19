# Lists, Tuples, Dictionaries and Sets
# Lists
# What are Lists? Lists are collection data types that can store thousands of data of different types.
#         0     1     2         3
# a = [1, 2, 3, 4, 5, 6]
# b = [i*3+3-5 for i in a]
#
# print(a)
# print(b)

# Tuples
# What are tuples? A tuple is a collection data type is immutable that allows you to duplicate elements
# my_fake_tuple = ['b', 'a', 'n', 'a', 'n', 'a', 's']
# print(type(my_fake_tuple))
#
# my_tuple = tuple(my_fake_tuple)
# print(type(my_tuple))
# print(len(my_tuple))
# print(my_tuple.index('s'))

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# b = a[::2]
# print(b)

# my_tupe = 'Ozichi', 10, 'Peinceley'
# name, age, name2 = my_tupe
# print(name)
# print(my_tupe)
#
# my_tuple = list((10, 3, 9))


# Dictionaries
# What are Dictionaries?
# Dictionaries are collection data types that are unordered and mutable. It consists of a collection of key-value pairs
# my_dict = dict(name='Ozichi', age=10)
# print(my_dict)
#
# # Excess a value
# print(my_dict['age'])
# my_dict['email'] = 'codewithozi@gmail.com'
# my_dict['email'] = 'codewithozi2@gmail.com'
# print(my_dict)
#
# del my_dict['age']
# print(my_dict)
#
# if 'name' in my_dict:
#     print(my_dict['name'])
#
# for key in my_dict.values():
#     print(key)
#
# my_cpy = dict(my_dict)
# my_cpy['age'] = 10
#
# print(my_dict)
# print(my_cpy)
#
# my_dict1 = {'name': 'Jack', 'age': 35, 'email': 'jakesbonne@gmail.com'}
# my_dict2 = {'name2': 'John', 'age2': 33, 'email2': 'johndoe@gmail.com'}
#
# my_dict1.update(my_dict2)
# print(my_dict1)

# Sets
# What are sets? A set is a collection data type that is unordered and mutable

# my_set = set()
#
# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
#
# print(my_set)
#
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}
#
# setA.symmetric_difference_update(setB)
# print(setA)
# Assignment?
# Build a simple key value data-base
# GET, POST, DELETE - Dictionary
