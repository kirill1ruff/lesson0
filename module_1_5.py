name='Immutable tuple:'
immutable_var = (1,2,3,'a','b')
print(name,immutable_var)
# Попытка изменить элементы кортежа immutable_var
#immutable_var[0] = 3
#Нельзя изменить значение элемента, потому что кортежи неизменяемы.
name='Mutable list:'
mutable_list = ['a','b',6,7,8,True,False,'a'+'b']
mutable_list[0]='Thank'
mutable_list[1]='you'
mutable_list[2]='for'
mutable_list[3]='the'
mutable_list[4]='opportunity'
mutable_list[5]='to'
mutable_list[6]='learn'
mutable_list[7]='programming'
print(name,mutable_list)



