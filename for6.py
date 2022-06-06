"""Diagrama y programa para averiguar e imprimir cuantos multiplos de 7y cuantos multiplos de 9 hay entre los numeros comprendidos entre 1000 y 5000"""

#Input
m = int(input("Digite el limite inferior: "))
n = int(input("Digite el limite superior: "))
#Processing
m_7 = 0
m_9 = 0
for i in range(m, n+1, 1):
    if i%7 == 0:
        m_7 += 1
    if i%9 == 0:
        m_9 += 1

#Output
print("--- Resultados ---")
print("Entre {m} y {n} hay")
print(f"{m_7} multiplos de 7")
print(f"{m_9} multiplos de 9")
