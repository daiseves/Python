import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic={}

while(len(colores)!=0):
    random.shuffle(colores)
    random.shuffle(coordenadas)
    clave=colores[0]
    valor=coordenadas[0]
    dic[clave]=valor
    colores.pop(0)
    coordenadas.pop(0)
    
print(dic)


