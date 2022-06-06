"""Generar la siguiente serie: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"""

#Input

#Processing
s = "Serie: ("
for i in range(1,11):
    if i < 10:
        s = s + str(i) + ", "
    else:
        s = s + str(i) + ")"

#Output
print("--- Resultados ---")
print(s)
