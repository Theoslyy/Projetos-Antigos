lista = list(map(int, input("Quais os elementos da lista? ").split(' ')))
lista2 = []
for i in range(len(lista)):
    lista2.append(lista[i]**2)
lista2.sort()
lista2.reverse()
print(lista2)   
print(max(lista2))
print(min(lista2))
print(sum(lista2)/len(lista2))