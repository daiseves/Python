import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]

dic={}
dicRandom={}

listaCoord=coordenadas.copy()
listaCol=colores.copy()

i=5
while(len(colores)!=0):
    num=random.randrange(i)
    clave=colores[num]
    valor=coordenadas[num]
    dic[clave]=valor
    colores.pop(num)
    coordenadas.pop(num)
    i=i-1
    
def suma():
    num1=random.randint(0,100)
    num2=random.randint(100,200)
    sumar=num1+num2
    texto= "¿Cuánto es {0} + {1}? :".format(num1, num2)
    resultado=int(input(texto))
    if resultado!=sumar:
        print("Incorrecto. El resultado es: ",sumar)
    else:
        print("El resultado es correcto")
        

def adivinaPalabra(lista):
    aux=random.randrange(3)
    print("Opciones de palabras: molesto, ratón, murciélago. La acentuación elegida es: ",lista[aux][0])
    resp=input("Ingrese respuesta: ")
    palabra=lista[aux][1]
    palabra=palabra[0]
    comp=lista[aux][1]
    comp=comp[0]
    if resp==comp:
        print("Congrats! La respuesta es correcta!")
    else:
        print("Meh, mala respuesta. La correcta era " ,comp)
        
for elem in listaCoord:
    color=random.choice(listaCol)
    dicRandom[elem]=color
    listaCol.remove(color)

print(dicRandom)

for coord, color in dicRandom.items():
    if color=='negro':
        suma()
    elif color=='blanco':
        adivinaPalabra(palabras)
    elif color=='amarillo':
        suma()
    elif color=='rojo':
        adivinaPalabra(palabras)
    elif color=='azul':
        suma()
