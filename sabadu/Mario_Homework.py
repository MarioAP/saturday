
# HOMEWORK: sort the items in the list from biggest import to smallest
lista = [45, 56, 55, 24, 57]
n = 0
for x in lista:
    n += 1
for i in range(n):
    for j in range(1, n-i):
        if lista[j-1] < lista[j]:
            (lista[j-1], lista[j]) = (lista[j], lista[j-1])
print(lista)
