jugadores={}

#POS 0 ES EL NOMBRE DEL JUGADOR POS 1 SON LOS ATRIBUTOS (OTRO DICC)

cant=int(input("¿Cuántos usuarios desea ingresar? "))

i=0
for i in range(cant):
    nombre = input('Ingrese nombre:')
    nivel=int(input('Ingrese nivel del juego:'))
    puntaje=int(input('Ingrese puntaje máximo:'))
    tiempo=int(input('Ingrese tiempo de juego:'))
    
    #Diccionario de diccionarios
    jugadores[nombre]={'nivel':nivel,'puntaje':puntaje, 'tiempo':tiempo}

print(jugadores)


def mejores10():
    aux= sorted(dic.items(), key=lambda punt: punt[1]['puntaje'],reverse=True)
    print(aux[:2])

def ordAlf():
    aux= sorted(dic.items(), key=lambda nomb: nomb[0])
    print(aux)

def ordNivel():
    aux= sorted(dic.items(), key=lambda level: level[1]['nivel'] ,reverse=True)
    print(aux)
    

print("10 primeros puntajes: ")
mejores10()
print("")
print("Ordenados alfabéticamente: ")
ordAlf()
print("")
print("Ordenados por nivel alcanzado: ")
ordNivel()
