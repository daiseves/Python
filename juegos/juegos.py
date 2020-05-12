import PySimpleGUI as sg
import os.path as path
from datetime import datetime
import json
import hangman
import reversegam
import tictactoeModificado

opciones = ('ahorcado', 'tateti', 'reverse')

#FUNCIÓN QUE AGREGA EL JUGADOR INGRESADP A LA ESTRUCTURA
def agregarJugador(nombre, juego, dic):
    dic[nombre]= juego

#FUNCIÓN QUE GUARDA LOS DATOS EN JSON
def guardarDatos(nombreArchivo, datos_guardar):
    d={}
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("Fecha y Hora =",dt_string)
    
    d[dt_string] = datos_guardar
    if path.exists(nombreArchivo):
        with open(nombreArchivo, 'r') as f:
            lista=json.load(f)
            lista.append(d)
        with open(nombreArchivo, 'w') as f2:
            json.dump(lista,f2)
    else:
        with open(nombreArchivo, 'w') as f3:
            lista=[d]
            json.dump(lista, f3)

#FUNCIÓN QUE MUESTRA EL ARCHIVO JSON
def mostrarArchivo(nom):
    with open(nom, 'r') as f: 
        data = json.load(f)
    print(json.dumps(data, indent=4))


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

#----------BUTTONS DE LAS VENTANAS---------- 
buttons = [[ sg.Button("Jugar", font=("Verdana", 10)), sg.Button("Mostrar datos", font=("Verdana", 10))]]
buttons2 = [[ sg.Button("Jugar", font=("Verdana", 10)),sg.Button("Cancelar", font=("Verdana", 10))]]
buttons3 = [[ sg.Button("Mostrar", font=("Verdana", 10)),]]


#----------PRIMER VENTANA DONDE PREGUNTO SI QUIERO JUGAR O MOSTRAR LOS DATOS---------- 
layout = [[sg.Text('¡Hola! ¿Qué preferís hacer?: ', size=(50,1), justification='center', font=("Verdana", 10))],             
          [sg.Column(buttons, justification='center')]]
         
window = sg.Window('Menú principal', layout)
event, values = window.Read()
window.close()

    
#----------EVENTOS DE LA PRIMERA VENTANA (JUGAR O MOSTRAR DATOS)---------- 
if event is 'Jugar':
    dic={}
    #----------SEGUNDA VENTANA DONDE ME PIDE LOS DATOS DEL JUGADOR---------- 
    layout2 = [[sg.Text('Nombre: ', size=(10, 1), justification='center', font=("Verdana", 10)), sg.Input(key='nombre')],      
               [sg.Text('Por favor, elige el juego que quieres jugar: ', size=(50, 1),justification='center', font=("Verdana", 10))],
               [sg.Listbox(opciones, size=(30, len(opciones)),  font=("Verdana", 10),  key='juego')],             
               [sg.Column(buttons2, justification='center')]]
    
    window = sg.Window('Datos del jugador', layout2)
    window.Finalize()
    
    while True:
        event, values = window.Read()
         #----------EVENTOS DE LA SEGUNDA VENTANA()---------- 
        if event is None:
            break
        if event is 'Cancelar':
            sg.popup('Adiós.')
            break
        if event is 'Jugar':
            juego=values['juego'][0]
            print('Vamos a jugar al ' ,juego)
            agregarJugador(values['nombre'], juego, dic)
            if __name__ == '__main__':
                import sys
                main(sys.argv)  
        #----------PREGUNTO SI QUIERO GUARDAR LOS DATOS DEL JUGADOR INGRESADO. SI ES AFIRMATIVO, LLAMA A LA FUNCION GUARDARDATOS()---------- 
        print('¿Quiere guardar los datos? y/n')
        op=input()
        if(op=='y'):
            print('Ingrese nombre del archivo: ')
            nom=input()
            guardarDatos(nom, dic)
            print('Datos guardados.')
        else:
            print('Ok')
            
#SI QUIERO MOSTRAR LOS DATOS DE LOS JUGADORES QUE YA JUGARON (EVENTO DE LA PRIMER VENTANA)
if event is 'Mostrar datos':
    #----------TERCER VENTANA DONDE PIDO QUE INGRESE EL NOMBRE DEL ARCHIVO QUE QUIERE MOSTRAR---------- 
    layout3=[[sg.Text('Ingrese nombre del archivo: ', justification='center', font=("Verdana", 10)), sg.Input(key='nombreArchivo')],[sg.Column(buttons3, justification='center')]]
    window = sg.Window('Mostrar Datos', layout3)
    window.Finalize()
    while True:
        event, values = window.Read()
        #----------EVENTOS DE LA TERCER VENTANA---------- 
        if event is 'Mostrar':
            aux=values['nombreArchivo']
            if path.exists(aux):
                mostrarArchivo(aux)
            else:
                sg.popup('El archivo no existe')      
        if event is None:
            break
        
        
