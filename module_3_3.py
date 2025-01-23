def print_params(a=1, b='строка', c=True):
    print(' ',a,b,c)

print("1.Вызовы функции с разным количеством аргументов:")
print_params()
print_params(2)
print_params(b='новая строка')
print_params(c=False)
print_params(3, 'ещё строка', False)
print_params(b = 25) #Работает
print_params(c = [1,2,3]) #Работает

values_list = [42, 'другая строка', False]
values_dict = {'a': 99, 'b': 'ещё одна строка', 'c': None}

print("\n2.Использование распаковки параметров:")
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print("\n3.Распаковка + отдельные параметры:")
print_params(*values_list_2, 42) #Работает