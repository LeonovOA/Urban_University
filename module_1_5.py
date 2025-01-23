# module_1_3.py

immutable_var = 1, 0.5, 'Tuple', True
print('Immutable Tuple: ' + str(immutable_var))
try:
    immutable_var[0] = 42
except TypeError as e:
    print('Error: ' + str(e))
mutable_list = [1, 0.5, 'list', False]
mutable_list[0] = 3
mutable_list[1] = 'Python'
print('Mutable list:' + str(mutable_list))