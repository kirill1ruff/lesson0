my_dict = {'Kirill': 1998, 'Svetlana':1981, 'Sergey': 1991}
print('My dict:',my_dict)
print('Existing value:',my_dict['Kirill'])
none_key = 'Evgeniy'
value_none_key = my_dict.get(none_key,'None')
print('Not existing value:',value_none_key)
my_dict.update({'Alena': 2002,
                'Andrey':1979})
removed_value = my_dict.pop('Sergey',"Key not found")
print("Delete volue:",removed_value)
print('Modified dictionary:',my_dict)
#
my_set = {1,2,3,True,3,4.375,2,1,6, 'Apple', True, 'Apple'}
print('Set:',my_set)
my_set.add(2.25)
my_set.add("Python")
my_set.pop()
print('Modified set:',my_set)
