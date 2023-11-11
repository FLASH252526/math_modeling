a, b, c = int(input()), int(input()), int(input())
if a >= b + c or b >= a + c or c >= a + b:
    print(f'Треугольника со сторонами {a}, {b}, {c} не существует')
else:
    if a == b == c:
        print(f'Треугольник со сторонами {a}, {b}, {c} - равносторонний')
    elif a == b != c or a == c != b or b == c != a:
        print(f'Треугольник со сторонами {a}, {b}, {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a}, {b}, {c} - разносторонний')