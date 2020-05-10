lista = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lista_nueva = []


for elem in lista:
    nombre, espacio, coordenadas = elem.partition(" ")
    coordenadas = coordenadas.split(',')
    
    for i, el in enumerate(coordenadas):
        coordenadas[i] = int(el)
        
    lista_nueva.extend([tuple(coordenadas)])
    
lista_nueva.sort()
print(lista_nueva)

