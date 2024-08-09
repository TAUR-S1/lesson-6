my_dict = {'Виктор': 1981,'Татьяна': 1978, 'Богдан': 2004}
print(my_dict)
print(my_dict['Виктор'])
my_dict['Дарина'] = 2013
print(my_dict['Дарина'])
my_dict.update({'Ольга': 1974,
                'Надежда': 1952})
del_ = my_dict.pop('Татьяна')
print(del_)
print(my_dict)

# Работа с множествами
my_set = {1, 0, 2, 8, 2, 8, 8, 'apple', 'coconut', 'apple', (1, 2, 3), (1, 2, 3)}
print(my_set)
my_set.add(6)
my_set.add(9)
my_set.discard('apple')
print(my_set)