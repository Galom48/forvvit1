import math as m

print( "Нахождение корней квадратного уравнения через дискриминант")
print("Внешний вид квадратного уравнения: ax^2 + bx + c = 0")

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

def Discriminant():
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + m.sqrt(discr)) / (2 * a)
        x2 = (-b - m.sqrt(discr)) / (2 * a)
        return f'x1 = {x1}, x2 = {x2}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'x = {x}'
    else:
        return "Корни квадратного уравнения отсутствуют"

print(Discriminant())
