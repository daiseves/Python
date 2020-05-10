EJERCICIO 3 (ver el orden de lista 2)
lista = ['Auto', '123', 'Viaje', '50', '120']
lista2=[]

for elem in lista:
    if elem.isdecimal():
        lista2.append(elem)


print(lista2)
lista2.sort()
print(lista2)
