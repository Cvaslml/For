"""Generar la siguiente serie: 1, 1/5, 1/10, 1/17, 1/26, ... n"""

#Input
n = int(input("Digite el valor de n:"))
#Processing
s = "Serie: ("
for i in range(1, n+1):
    t = i**2 + 2*i + 2
    if i < n:
        s = s + "1/" + str(t) + ", "
    else:
        s = s + "1/" + str(t) + ")"

#Output
print("--- Resultados ---")
print(s)
