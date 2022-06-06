"""Generar la siguiente serie: 2, 4, 8, 32, 64, ... n"""

#Input
n = int(input("Digite el valor de n:"))
#Processing
s = "Serie: ("
for i in range(1, n+1):
    t = 2**i
    # t = i*i
    if i < n:
        s = s + str(t) + ", "
    else:
        s = s + str(t) + ")"

#Output
print("--- Resultados ---")
print(s)
