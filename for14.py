"""Generar la siguiente serie: 2, 6, 12, 20, 30, 42, 56, ... n"""

#Input
n = int(input("Digite el valor de n:"))
#Processing
s = "Serie: ("
for i in range(0, n+1):
    t = i**2 + 3*i + 2
    if i < n:
        s = s + str(t) + ", "
    else:
        s = s + str(t) + ")"

#Output
print("--- Resultados ---")
print(s)
