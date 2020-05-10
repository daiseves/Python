tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista1=[]
lista2=[]


num=int(input('Ingrese un número:'))


for elem in tam:
    nombre, espacio, coordenadas = elem.partition(' ')
    coordenadas = coordenadas.split(',')
    
    for i, el in enumerate(coordenadas):
        coordenadas[i] = int(el)
        
    aux=int(coordenadas[0])
    if(aux>=num):
        lista1.extend([nombre, tuple(coordenadas)])
    else:
        lista2.extend([nombre, tuple(coordenadas)])
        
print('Lista con números mayores o iguales a' , num , ':' , lista1)
print('Lista con números menores a' , num , ':' , lista2)

    
