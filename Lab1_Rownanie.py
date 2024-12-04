import math

print("Wpisz współczynniki równania kwadratowego a, b ,c")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def delta(a: float, b: float, c: float):
    return float(math.pow(b,2) - 4*a*c)

def pierwiastki(a: float, b: float, c: float):
        d = delta(a, b, c)
        #drukujemy wartość delty
        print("d = " + str(d))
        try:
            if d == 0:
                x = -b / (2 * a)
                print("x = " + str(x))
            elif d < 0:
                print("brak pierwiastków")
            else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                print("x1 = " + str(x1), "x2 = " + str(x2))
        except ZeroDivisionError:
            print("a nie może być = 0")

pierwiastki(a, b, c)