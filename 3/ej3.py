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

#inciso b
impdatos = input('Ingrese nombre del jugador del que desea imprimir datos:')
print (jugadores.get(impdatos, 'El usuario no existe'))

#inciso c
print("Nombres de los usuarios que jugaron: " ,jugadores.keys())

#inciso d
ganador = max(jugadores.items(), key=lambda jugador: jugador[1]['puntaje'])
print('Nombre del jugador con puntaje máximo: ' ,ganador[0])

#inciso e
ordenados=sorted(jugadores.items(), key=lambda jugador: jugador[1]['puntaje'], reverse=True)
print(ordenados)


nombre_jugador = input("Ingrese nombre del Jugador de la jugada: ")
puntaje_jugada = input(f"Ingrese puntaje de la jugada de {nombre_jugador}: ")
nivel_jugada = input(f"Ingrese nivel de la jugada de {nombre_jugador}: ")
tiempo_jugada = input(f"Ingrese tiempo de la jugada de {nombre_jugador}: ")
juga_nuevo = {'nivel': nivel_jugada, 'puntaje': puntaje_jugada, 'tiempo': tiempo_jugada}
jugadores.setdefault(nombre_jugador,juga_nuevo)
print(jugadores)

jugadoresXL_or = sorted(jugadores_nuevos.items(), key=lambda punt: punt[1]['puntaje'],reverse=True)
jugadoresXL_or[:10]
