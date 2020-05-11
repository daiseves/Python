import PySimpleGUI as sg
import os.path as path
from datetime import datetime
import json
import hangman
import reversegam
import tictactoeModificado

opciones = ('ahorcado', 'tateti', 'reverse')

def guardarDatos(clave, nombre, datos_guardar):
    d={}
    
    #ANOTACION 1
    # dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # print("Fecha y Hora =",dt_string)
    # d[dt_string] = datos_guardar
    
    d[clave] = datos_guardar
    
    with open(nombre, 'r') as f:
        lista=json.load(f)
        lista.append(d)
    with open(nombre, 'w') as f2:
        json.dump(d,f2)
        
def mostrarArchivo(nom):
    with open(nom, 'r') as f: 
            #Se abre un archivo y procesa utilizando el método json.load()
            data = json.load(f)
            print(json.dumps(dato, indent=4))

def main(args):
        opcion=values['juego'][0]
        if opcion == 'ahorcado':
            hangman.main()
        elif opcion == 'tateti':
            tictactoeModificado.main()
        elif opcion == 'reverse':
            reversegam.main()
        print('Hasta la próxima :)')
        
        
#MENÚ DEL JUEGO        

sg.theme('LightBlue6')
layout = [
          [sg.Text('Nombre: ', size=(10, 1), justification='center', font=("Verdana", 10)), sg.Input(key='nombre')],      
          [sg.Text('Edad: ', size=(10, 1), justification='center', font=("Verdana", 10)), sg.Input(key='edad')],
          [sg.Text('Por favor, elige el juego que quieres jugar: ', size=(50, 1),justification='center', font=("Verdana", 10))],
          [sg.Listbox(opciones, size=(15, len(opciones)), key='juego')],             
          [sg.Button('Jugar' ),sg.Button('Cancelar')]                   
         ]


listaCant=[]
print("1: Jugar.")
print("2: Mostrar datos de juego.")
choice=int(input())

#SI DECIDO JUGAR    
if choice==1:
    window = sg.Window('Datos del jugador', layout)
    window.Finalize()
    while True:
        event, values = window.Read()
        #De acá en más identifico los eventos de mi ventana y digo qué quiero que haga cada evento
        if event is None:
            break
        if event is 'Cancelar':
            sg.popup('Adiós.')
            break
        if event is 'Jugar':
            juego=values['juego'][0]
            print('Vamos a jugar al ' ,juego)
            # listaCant.append((values['nombre'], values['edad'], juego))   ANOTACION 1
            listaCant.append((values['edad'], juego))
            if __name__ == '__main__':
                import sys
                main(sys.argv)  
        print('¿Quiere guardar los datos? y/n')
        op=input()
        if(op=='y'):
            clave=values['nombre']
            print('Ingrese nombre del archivo: ')
            nom=input()
            guardarDatos(clave, nom, listaCant)
            print('Datos guardados.')
        else:
            print('Ok')
#SI QUIERO MOSTRAR LOS DATOS DE LOS JUGADORES QUE YA JUGARON
elif choice==2:
    nombre = input("Ingrese nombre del archivo a mostrar:  ")
    if path.exists(nombre):
        mostrarArchivo(nombre)
    else:
        print('El archivo no existe')
        
        
        
        
#ANOTACION 1: Esas lineas de código comentadas generan que la clave de mi diccionario sea la fecha y hora en la que el usuario jugó y
#agrega a mi lista todos los datos del usuario (nombre, edad y el juego que prefirió).
#Si, en cambio, decido no ponerle la fecha y la hora, la clave de mi diccionario va a ser el nombre del jugador y mi lista guardará los datos de su edad y el juego que prefirió.

