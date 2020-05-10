import random


colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic={}
i=5

while(len(colores)!=0):
    num=random.randrange(i)
    print(num)
    clave=colores[num]
    valor=coordenadas[num]
    dic[clave]=valor
    colores.pop(num)
    coordenadas.pop(num)
    i=i-1
    
print(dic)
