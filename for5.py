"""Hacer el diagrama de flujo y el programa en Python que genere 1000 numeros aleatorios y que averigue e imprima cuantos son pares y cuantos son impares"""

print("--------------------------------------------")
print("--------------PARES E IMPARES---------------")
print("--------------------------------------------")
import random
# input
pares = 0
impares = 0

#Processing
for i in range(1000):
    num_aleatorio = random.randit(1,200)
    if num_aleatorio%2 == 0:
        pares += 1
    else:
        impares += 1

#Output
print("Resultados: ")
print(f"Cantidad de pares = {pares}")
print(f"Cantidad de impares = {impares}")