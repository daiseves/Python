from random import shuffle
p = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]

correctas=0
shuffle(p)
while (len(p)!=0):
        print('¿',p[0][0],'?',end= "")
        respuesta = input(" Si o no ")
        respuesta=respuesta.lower()
        respuesta2=p[0][1]
        print(respuesta2)
        if respuesta == respuesta2:
            print('Respuesta Correcta')
            correctas=correctas+1
        else:
            print("Respuesta Incorrecta")
        p.pop(0)
print("Cantidad de respuestas correctas" ,correctas)
