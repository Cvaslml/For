"""Programa para digitar el nombre y cuente cuantas vocales hay en el nombre. Con la funcion for"""

print("------------------------------------")
print("--------Contador de vocales---------")
print("------------------------------------")

#Input
n = input("Digite su nombre: ")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for vocal in n:
    if vocal.lower() in "a":
        contador_a += 1
    elif vocal.lower() in "e":
        contador_e += 1
    elif vocal.lower() in "i":
        contador_i += 1
    elif vocal.lower() in "o":
        contador_o += 1
    elif vocal.lower() in "u":
        contador_u += 1
print("El nombre " + str(n) + " contiene " + str(contador_a) + " vocales a, " + str(contador_e) + " vocales e, " + str(contador_i) + " vocales i, " + str(contador_o) + " vocales o, " + str(contador_u) + " vocales u ")

    