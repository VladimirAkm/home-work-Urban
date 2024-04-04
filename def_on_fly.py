print('Задача 1: Фабрика функций')


def func_factory(operation):
    if operation == 'summ':
        def summ(a, b):
            return a + b

        return summ

    elif operation == 'divide':
        def divide(a, b):
            return a / b

        return divide
    else:
        raise Exception


funcs_names = ['summ', 'divide']
lst = [func_factory(i) for i in funcs_names]
for func in lst:
    print(func(4, 2))

print('Задача 2: Лямбда')

multiply = lambda x, y: x ** y
print(multiply(4, 2))


def multiply_def(x, y):
    return x ** y


print(multiply_def(4, 2))

print('Задача 3: Вызываемые объекты')

class rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self, ):
        return self.breadth * self.length


obj = rectangle(2, 4)
print('Стороны: ', 2, 4)

print('Площадь :', obj.area())
