print(jugadores.keys())
print(jugadores.values())
print(jugadores.items())
print("Nombres de los usuarios que jugaron: " ,dict.keys())

#max
ganador = max(jugadores.items(), key=lambda jugador: jugador[1]['puntaje'])
print(ganador[0])

podio=sorted(jugadores.items(), key=lambda jugador: jugador[1]['nivel'], reverse=True)
print(podio[:3])
print("{} con nivel {}".format(podio[0][0],podio[0][1]['nivel']))


jug_ordebados=sorted(jugadores.items(), key=lambda jugador: jugador[1]['nivel'], reverse=True)
podio= jug_ordebados[:3]
nombres_podio=jug for jug in podio]
print(nombres_podio)


nombres_podio = [len(jug[0]) for jug in podio if jug[1]['tiempo']>4000]  #itera con jugador y devuelve un valor
print(nombres_podio)
