"""Generar la siguiente serie: 1, 4, 9, 16, 25, 36 ... n"""

#Input
n = int(input("Digite el valor de n:"))
#Processing
s = "Serie: ("
for i in range(1, n+1):
    t = i**2
    # t = i*i
    if i < n:
        s = s + str(t) + ", "
    else:
        s = s + str(t) + ")"

#Output
print("--- Resultados ---")
print(s)
