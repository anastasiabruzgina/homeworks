# тут все мои homeworks

а это - личная шпора
cкрещиваем два списка в list с помощью zip

a = [i*2 for i in range(1,5)]
b = [i for i in range(1,5)]

c = list(zip(a, b))
print(a, b, c)

list(map(функция(которая выполнится над каждым элементом), range(x)))

Анонимные функции:
list(filter(lambda x: x > o, range(-2, 3)

from funtools import reduce
reduce(lambda x, y: x * y, range(1, 5)

списочные выражения:
square_map = {num: num ** 2 for num in range(1,5)} словарик имеем

или 
square_map = [num ** 2 for num in range(1,5)] 

генераторы - yield
