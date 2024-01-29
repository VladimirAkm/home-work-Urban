# Функции с параметрами по умолчанию :
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(b, c)
    print(a, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров :
values_list = [1, 'строка', True]
res = print_params(*values_list)
print(res)
values_dict = {'a': 1, 'b': 'строка', 'c': True}
res = print_params(**values_dict)
print(res)
