import math


#aqui calculo el area del cuadrado
def area_cuadrado(lado):
    return lado ** 2
#aqui calculo el area del triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2
#aqui calculo el area del circulo
def area_circulo(radio):
    return math.pi * (radio ** 2)

#1º requerimiento - Dos círculos de radio 10 + un triángulo de base 3 y altura 7
area_circulo_1 = area_circulo(10)
area_circulo_2 = area_circulo(10)
area_triangulo_1 = area_triangulo(3, 7)

print(area_circulo_1)
print(area_circulo_2)
print(area_triangulo_1)

area_total_1 = area_circulo(10) + area_circulo(10) + area_triangulo(3,7)
#area_total_1 = area_circulo_1 + area_circulo_2 + area_triangulo_1
print("El área total es:", area_total_1)

#2º requerimiento - Un cuadrado de lado = 10 + 3 círculos (uno de radio = 4 y los otros dos de radio = 6) + 5 triángulos de base = 2 + altura = 4
area_cuadrado_2 = area_cuadrado(10)
area_circulo_3 = area_circulo(4)
area_circulo_4 = area_circulo(6)
area_circulo_5 = area_circulo(6)
area_triangulo_2 = area_triangulo(2, 4)

print(area_cuadrado_2)
print(area_circulo_3)
print(area_circulo_4)
print(area_circulo_5)
print(area_triangulo_2)

area_total_2 = area_cuadrado(10) + (area_circulo(4) + area_circulo(6) + area_circulo(6)) + 5 * area_triangulo(2, 4)
#area_total_2 = area_cuadrado_2 + (area_circulo_3 + area_circulo_4 + area_circulo_5) + 5 * area_triangulo_2
print("El área total es:", area_total_2)