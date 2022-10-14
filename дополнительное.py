massiv = list(map(float,input("Введи массив через пробел").split()))
minimum = min(massiv)
delta = float(input("Дельта: "))
print(massiv.count(delta + minimum))
