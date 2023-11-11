import math
a, b, c = int(input()), int(input()), int(input())
if b ** 2 - 4 * a * c >= 0:
    x1 = (b * (-1) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (b * (-1) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
else:
    print('Корней нет')
if x1 == x2:
    print('Один корень -', x1)
else:
    print(f'Два корня - {x1}; {x2}')