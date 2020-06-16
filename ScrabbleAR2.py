import PySimpleGUI as sg
import string
from random import shuffle
from pattern.es import tag, spelling, lexicon, verbs
import copy

valores_letras = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5,
                 "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4,
                 "W": 4, "X": 8, "Y": 4, "Z": 10, "#": 0}

primer_ronda= [(4,5),(5,4),(5,6),(6,5)]           

imagesX2 = [(0,10), (1,9), (2,8), (3,7),(4,6),(5,5),(6,4),(7,3),(8,2),(9,1),(10,0)]
imagesx3 = [(0,0), (1,1), (2,2), (3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

#----------------------- CLASE FICHA -----------------------

class Ficha:
    def __init__(self, letra, valores_letras):
        self.letra = letra
        self.valor = valores_letras[self.letra]
            
    def retornar_letra(self):
        return self.letra
            
    def retornar_valor(self):
        return self.valor

#----------------------- CLASE BOLSA -----------------------

class Bag:
    def __init__(self):
        self.bag=[]
        self.letras = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ#')
        self.repeticiones = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,2,2,2,2,1,2,1,2]
        self.anexo()
        #valores = [1,3,3,2,1,4,2,4,1,1,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10,0]
        
    def anexo(self):
        global valores_letras
        for letra, cantrep in zip(self.letras, self.repeticiones):
            for i in range (cantrep):
                self.bag.append(letra)
          
          # print(Ficha(letra,valores_letras).retornar_valor())           Retorna el valor de la letra
          
        #Desordena las letras de la bolsa
        shuffle(self.bag)
        print(self.bag)
     
    #elimina una ficha y la retorna
    def dar_ficha(self):   
        return self.bag.pop()
    
    #Me devuelve el número de fichas que tiene la bolsa    
    def actualiza_bolsa(self):
        aux=len(self.bag)
        return aux


#----------------------- CLASE ATRIL -----------------------

class Atril:
    def __init__(self, Bag):
        self.bag=Bag
        self.atril=[]
     
    def agregar_fichas(self):
        for i in range(7):
            self.atril.append(self.bag.dar_ficha())
        return(self.atril)
 
    def soltar_ficha(self, ficha):
        self.atril.remove(ficha)
    
    #Devuelve número de fichas que quedan en el atril
    def fichas_en_atril(self):
        aux=len(self.atril)
        return aux
 
    #Mientras la bolsa tenga fichas, repone el atril para que siempre tenga 7 fichas
    def reponer_ficha(self):
        while self.fichas_en_atril() < 7 and self.bag.actualiza_bolsa()>0:
            self.atril.append(self.bag.dar_ficha())
            
    def atril_array(self):
        #Devuelve el atril como un array
        return self.atril
            

#----------------------- CLASE PALABRA -----------------------
class Palabra:
    def __init__(self, word, jugador):
        self.word=word
        self.jugador=jugador
        
        self.convert()
        
        
    def convert(self):
        self.new=""
        for letra in self.word:
            self.new+=letra
        
        if not self.new.lower() in verbs:
            #print('La palabra NO está en verbs.')
            if (self.new.lower() in lexicon) and (self.new.lower() in spelling):
                #print('La palabra si existe.')
                ok = True
            else:
                #print('La palabra ingresada no existe.')
                ok = False
        else:
            #print('La palabra si existe.')
            ok = True
        return ok

    def calcular_puntaje(self):
        global valores_letras
        puntaje=0
        for letra in self.new:
            puntaje += valores_letras[letra]
        print(puntaje)
        self.jugador.aumentar_puntaje(puntaje)
        
            
    
    
#----------------------- CLASE JUGADOR -----------------------
class Jugador:
    def __init__(self, bag, name):
        self.atril = Atril(bag)
        self.puntaje = 0
        self.name=name
        
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def aumentar_puntaje(self, aumento):
        self.puntaje += aumento

    def get_puntaje(self):
        return self.puntaje
        
    def get_atril(self):
        return self.atril.get_atril()
        
    def atril_array(self):
        return self.atril.atril_array()
 

        
def jugar(jugador, bag, tablerogame, ficha_central):
    global cant_rondas, m, s
    filas=11
    columnas=11
    atrilInterfaz=[]
        
    sg.theme_background_color('#E5CEAC')

    #-----CREAMOS LAS COLUMNAS--------   
    columna1=[[sg.Text('-'*70,background_color='#D2B3BB')],
                [sg.Button('Validar', button_color=('white','saddlebrown'), size=(10, 2), font=("Verdana", 10)), sg.Button('Terminar turno',  button_color=('white','saddlebrown'), size=(10, 2), font=("Verdana", 10)), sg.Button('Salir', button_color=('white','saddlebrown'),  size=(10, 2), font=("Verdana", 10))],
                [sg.Text('  ',background_color='#D2B3BB')],
                [sg.Text('Puntaje de la palabra ingresada', font='Default 10', justification='center', background_color='#D2B3BB')],
                [sg.Multiline([], do_not_clear=True, autoscroll=True, size=(37,5),key='_puntaje_')],
                [sg.Text("",background_color='#D2B3BB')],
                [sg.Text('Puntaje Total', font='Default 10', justification='center', background_color='#D2B3BB')],
                [sg.Multiline([], do_not_clear=True, autoscroll=True, size=(37,10),key='_puntajeTotal_')],
                [sg.Image(r'C:\Users\lara\Desktop\Python\pythonWord.png',background_color='#D2B3BB')]
                ]
    columna2=[]
    columna2+=tablerogame
    columna2+=atrilInterfaz
        
    layout = [[sg.Column(columna1, size=(300,600),background_color='#D2B3BB'), sg.Column(columna2,size=(470,600), background_color='#E5CEAC')]]
    window = sg.Window('TABLERO SCRABBLE', layout, location=(130,0))
        
        
    if (bag.actualiza_bolsa()!=0):
        sg.popup('Es el turno del jugador: ' ,jugador.get_name(), background_color='#FFE0A3', text_color='saddlebrown')
        
        
    sigue=True
    listaLetras=[]
    dicc2 = {}   
    dicc2[(m,s)]=ficha_central
          
    while True:
        #-----AGREGO EL ATRIL--------
        if jugador.get_name()=='PC':
            window.FindElement(atrilInterfaz).update(sg.Button(jugador.atril_array()[row], size=(4,2), key=(row), font='verdana 14', button_color=('saddlebrown','#FFE0A3'))for row in range(7))
        else:
            window.FindElement(atrilInterfaz).update(sg.Button(jugador.atril_array()[row], size=(4,2), key=(row), font='verdana 14', button_color=('saddlebrown','#FFE0A3'))for row in range(7))
            
        event, values = window.Read()           
        if event in (None, 'SALIR'):
            break

        #-----EVENTOS DEL ATRIL-----
        elif event in (0,1,2,3,4,5,6):
            aux = jugador.atril_array()[event]
            vacio = copy.deepcopy(event)
            event, values = window.read()
                
            if cant_rondas==1 and sigue:                       
                if event not in primer_ronda:
                    sg.popup('Error. La primer ficha debe ir en las coordenadas (4,5),(5,4),(5,6) o (6,5)',background_color='#D2B3BB')

                else:      
                    dicc2[event] = aux              
                    window.FindElement(vacio).update("",button_color=('saddlebrown','#FFE0A3')) 
                    window.FindElement(event).update(aux, button_color=('saddlebrown','#FFE0A3')) 
                    sigue=False
                        
            elif event not in dicc2.keys():
                dicc2[event] = aux                  #aux es la letra de la ficha                #diccionario 2 guarda las coordenadas donde esta cada letra en el tablero
                window.FindElement(vacio).update("",button_color=('saddlebrown','#FFE0A3')) 
                window.FindElement(event).update(aux, button_color=('saddlebrown','#FFE0A3')) 
            else:
                sg.popup('El casillero ya se encuentra ocupado.', title=':(',background_color='#D2B3BB')
            dicc2Ord=dict(sorted(dicc2.items()))
                
        if event is 'Validar':
            for elem in dicc2Ord.values():
                listaLetras.append(elem)
            palabra=Palabra(listaLetras, jugador)
            lista=listaLetras.copy()
            if palabra.convert():
                palabra.calcular_puntaje()
                window.FindElement('_puntaje_').update("Valor de la palabra: {}".format(jugador.get_puntaje()))
                window.FindElement('_puntajeTotal_').update()
                #ElIMINA DEL ATRIL LAS LETRAS QUE USÓ
                for letra in jugador.atril_array():
                    if letra in lista:
                        jugador.atril.soltar_ficha(letra)
                        
            else:
                sg.popup('La palabra ingresa no existe.',background_color='#FFE0A3', text_color='saddlebrown')
                
                
    
            #-----REPONGO LAS FICHAS QUE LE FALTAN AL JUGADOR-----
            jugador.atril.reponer_ficha()
            
            #-----PASA AL SIGUIENTE TURNO-----
            if jugadores.index(jugador) != (len(jugadores)-1):
                jugador = jugadores[jugadores.index(jugador)+1]
            else:
                jugador = jugadores[0]
                cant_rondas += 1
             
             
            window.finalize()  


def inicio():
    global jugadores, cant_rondas, m, s
    tablerogame=[]
    filas=11
    columnas=11
    bag = Bag()

    
    #-----ESQUELETO DEL TABLERO-------- 
    for fila in range(filas):
        layout_fila = []
        for col in range(columnas):
            layout_fila.append(sg.Button(' ', size=(4, 2), key=(fila,col), pad=(2,2), button_color=('peachpuff','white')))
        tablerogame.append(layout_fila)
        
    sg.theme_background_color('#E5CEAC')
    
    layout = [
              [sg.Image(r'C:\Users\lara\Desktop\Python\ScrabbleWord.png', size=(1000,300),background_color='#E5CEAC')],
              [sg.Text('NOMBRE:', font ='centaur 30', size=(13,1), justification='center',background_color='#E5CEAC'), sg.InputText(key='__nombre__',size=(30,1), font='Courier 30')],
              [sg.Button('INICIAR', button_color=('white','saddlebrown'), font='centaur 30', pad=((420,0),(30,50)), size=(12,1),)],
             ]

    window = sg.Window('Bienvenido', layout, size=(1100,500), location=(200,60))

    while True:
        event, values = window.Read()
        if event is None:
            break
        if event is 'INICIAR':
            window.close()
            nom=values['__nombre__']
            #INSTANCIO LOS DOS JUGADORES
            jugador1 = Jugador(bag, nom)
            jugador2 = Jugador(bag, 'PC')
            #LES REPARTO FICHAS PARA EL ATRIL
            jugador1.atril.agregar_fichas()
            jugador2.atril.agregar_fichas()
            #LOS AGREGO A UNA LISTA
            jugadores = []
            jugadores.append(jugador1)
            jugadores.append(jugador2)
            #random.shuffle(jugadores)       desordeno para no saber quién empieza el turno
            
            
            #-----BONUS EN EL TABLERO--------   
            for i in imagesX2:
                f=i[0]
                c=i[1]
                tablerogame[f][c]=sg.Button(image_filename=r'C:\Users\lara\Desktop\Python\x2.png', image_size=(37, 37), size=(4, 2), key=(f,c), pad=(2,2), button_color=('white', '#79B7BF'))
            
            for j in imagesx3:
                f=j[0]
                c=j[1]
                tablerogame[f][c]=sg.Button(image_filename=r'C:\Users\lara\Desktop\Python\x3.png', image_size=(37, 37), size=(4, 2), key=(f,c), pad=(2,2), button_color=('white', '#D2B3BB'))
        
            tablerogame.append([sg.T('', background_color='#E5CEAC')] + [sg.T('{}'.format(a), pad=((2, 25),2), font='Any 13', background_color='#E5CEAC') for a in 'ABCDEFGHIJK'])
            
            
            #INICIALIZO VARIABLES GLOBALES
            cant_rondas=1
            jugador_actual = jugadores[0]  
            m=int(filas-1)//2
            s=int(columnas-1)//2
            
            #-----FICHA EN EL CENTRO-------- 
            ficha_central=bag.dar_ficha()
            tablerogame[m][s]=sg.Button(ficha_central,size=(4, 2), key=(m,s), pad=(2,2), button_color=('saddlebrown','#FFE0A3'))
            
            jugar(jugador_actual, bag, tablerogame, ficha_central)

inicio()


#main principal - 5 lineas donde importo las clases
