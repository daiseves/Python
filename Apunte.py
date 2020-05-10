>>>Me dice el tipo de dato
print(type(algo))

>>>Paso todo a minúsculas o mayúsculas e imprimo
listaMin=lista.lower()
listaMay=lista.upper()

>>>Pido número por teclado
num=int(input('Ingrese un número:'))

>>>Pido string por teclado
print("¿Cómo se llama?")
nombre = input()

>>>Conversión
print(ord('ć'))   #263   -> convierte un caracter en int 
print(chr(65))    #A     -> convierte un int en caracter

>>> /n (new line, salto de linea)
	print("\n Hola {0}!! \n\nHoy es {dia} de {mes}".format("chicos", dia=14, mes="abril"))


>>>FOR : para recorrer hasta un num entero
	for i in range(cant):

>>>Genero números random >=100  // Antes de usarlo, tengo que importar la función: import random
import random
numaleatorio= random.randrange(100)

>>>Para imprimir por pantalla texto y variables:
print ('Ganaste! y lo hiciste en', cont, 'intentos!')
print ('\n Perdiste :(\n La compu pensó en el número:', numero_compu)


>>>LISTAS
	lis2 = lis1 hace que el lis2 apunte a lis1 (ambos apuntan a la misa zona de memoria)
	lis2 = lis[:] hace que dos direcciones de memoria tengan el mismo contenido

	->Agregar elemento a una lista
			lista.append(6)
	-> Agregar valores:
			a = [1, 3, 5, 7]
			a.append(9)
	-> Agregar valor en posición específica
			a = [1, 3, 4, 5, 6]
			a.insert(1, 2)                 
			#[1, 2, 3, 4, 5, 6]
	-> Elimiar elementos
			a = ["Perro", "Gato", "Caballo"]
			a.remove("Gato")
	-> Eliminar elemento ´por posición
			a = ["Manzana", "Pera", "Banana", "Naranja"]
			del a[1]
			#['Manzana', 'Banana', 'Naranja']
	-> Eliminar todos los elementos
			del a[:]
			
	-> Creo una lista con los elementos de una frase separados por un string ingresado por teclado
			lista=frase.split(string)

	-> Ordeno los elementos de una lista
			nombres_masculinos.sort() 

	-> Copio elementos de una lista a otra
			lista = [ 22, True, 'una lista', [1,7] ]
			lis1 = lista.copy()

	-> Sumo elementos a una lista
			lis2 = lis1 + [9,8,7]

	-> Multiplico los elementos de una lista (quedan los elementos repetidos). Se almacenan punteros a las mismas posiciones. 
	   Por lo que si modifico un elemento, modifico todos los que están repetidos 
			lis2 = lis1 * 2 

	-> RANGE: función que devuelve lista de enteros. No tiene en cuenta el último valor de los rangos
	   Estos dos ejemplos dan el mismo resultado:

			valorFinal=4                                 valorFinal=4
			i=0                                          i=0
			while i <= valorFinal:                       for i in range (i, valorFinal + 1):
    			print('algo')								print('algo')
    			i += 1


>>>TUPLAS:colecciones de datos ordenados
	tupla1 = 1,2
	tupla1 = (1,2)
	-> Si se quiere crear una tupla con un único elemento, debe añadirse una coma (,) antes de cerrar el paréntesis
			b = (5,)
	-> .index : Buscar elemento y saber su pos. Da error si no lo encuentra
			tupla.index(100)
			tupla.index('Hola')
	-> .count : Para saber cuántas veces aparece un elemento en la tupla
			tupla.count(100)
			tupla.count('Algo')
	-> Último elemento de la tupla se encuentra en la pos a[len(a) - 1] ya que comienza en 0
	-> Convertir lista en tupla 
			a = tuple(a)
	-> Convertir tupla en lista
			a = list(a)
	-> Buscar elemento con in   (si no existe not in)
			a = (1, 2, 3, 4)
			3 in a             #True
			5 in a 			   #False

			"CPython" in ["PyPy", "Stackless", "IronPython"]       #False




>>>SET:colección de datos de igual o diferente tipo, desordenada y sin elementos duplicados
	Operaciones con conjuntos (las mismas que en los Conjuntos)
	• in ve si un elemento pertenece al conjunto. Devuelve true o false 
			colores_calidos = set (["celeste", "rosa"])
			print("azul" in colores_calidos)   -> devuelve false
	• | permite la unión entre dos conjuntos.
			todos = colores_calidos | colores_fuertes
    • & permite la intersección entre dos conjuntos.  -> devuelve set() si el conjunto queda vacío
    		x = colores_calidos & colores_fuertes

    Operaciones sobre conjuntos 
    	conju1 = set([1, 2, 3, 4])
		conju2 = conju1

    	•copy()      -> copia conjuntos                             conju3 = conju1.copy()
   		•add()       -> agrega elementos al conjunto                conju1.add(7)
   		•discard()   -> elimina elemento del conjunto               conju1.discard(1)



>>>DICCIONARIO: estructuras de datos que permite guardar un conjunto no ordenado de pares clave-valor, siendo las claves únicas dentro de un mismo diccionario
	->Agregar elemento: 
			diccionario[clave] = valor
	->Diccionario de diccionario (los valores son variables que leí por teclado): 
			jugadores[nombre]={'nivel':nivel,'puntaje':puntaje, 'tiempo':tiempo}
	->dic.items() : devuelve lista de tupla (el primer elemento es la clave, el segundo el valor)
	->dic.keys(): retorna lista de elementos que son las claves
	->dic.values(): retorna una lista de elementos que son los valores
	->dic.clean(): elimina todos los elementos del diccionario
	->dic.copy(): hace una copia del diccionario
	->dic.get('clave'): recibe una clave como parámetro y devuelve su valor. Devuelve none si no lo encuentra. Sin comillas si es una variable
	->dic.pop('clave'): Elimina la clave que recibe como parámetro y devuelve su valor. Sin comillas si es una variable
	->dic.update(nomDeOtroDic): Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; 
	  si no hay claves iguales, este par clave-valor es agregado al diccionario.
	->dict.has_key(key) : Devuelve true si existe la clave, false si no.
	->sorted(dic) : ordena el diccionario por claves
	->sorted(dic.items()): devuelve lista con todos los elementos del diccionario

>>>FUNCIONES: Bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, 
              la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea, este bloque puede ser llamados cuando se necesite.
	-> Sintaxis:
		def nombre (parámetros):
    		sentencias
    		return [expresión/variable]

	-> Envía lista como parámetro
    	def sumar(numbers):
    		result = 0
    		for number in numbers:
      		    result += number
    		print result
		sumar([4,5])

	-> Envía diccionario como parámetro
		def sumar(**numbers):
   		    print numbers
    	    print numbers['number1'] + numbers['number2']
		sumar(number1=10, number2=20)

	-> Argumentos indeterminados/por posición: Para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos (una tupla) 
	   definiendo el parámetro con un asterisco
		def indeterminados_posicion(*args):
    		for arg in args:
        		print(arg)
		indeterminados_posicion(5,"Hola",[1,2,3,4,5])
	-> Argumentos indeterminados/por nombre: Para recibir un número indeterminado de parámetros por nombre (clave-valor/keyword args), debemos crear un diccionario dinámico 
	   de argumentos definiendo el parámetro con dos asteriscos:
		def indeterminados_nombre(**kwargs):
    		for kwarg in kwargs:
        		print(kwarg, "=>", kwargs[kwarg])
		indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])
	-> Argumentos indeterminados/por posición y por nombre:Si queremos aceptar ambos tipos de parámetros simultáneamente, debemos crear ambas colecciones dinámicas. 
	   Primero los argumentos indeterminados por valor y luego los que son por clave y valor:
		def super_funcion(*args,**kwargs):
   			total = 0
    		for arg in args:
        		total += arg
    		print("sumatorio => ", total)
    		for kwarg in kwargs:
        		print(kwarg, "=>", kwargs[kwarg])
		super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)


	-> .format 
		Nombre = input(str("Ingresa tu nombre \n"))
		Edad = int(input("Bien, ahora ingresa tu edad \n"))
		NombreMascota = input(str("Ingresa el nombre de tu mascota \n"))
		print ("Tu nombre es {0} y tienes {1} años. Tu mascota se llama {2}".format(Nombre, Edad, NombreMascota))

		*Colocamos las llaves donde se mostrará el contenido de la variable y dentro de ellas un número que corresponde con el orden de la variable dentro de la función format.
		 Los números de identificación (0,1,2) nos permiten repetir el uso de la variable indicando cual de ellas.


	-> Map: 
		->Ejecuta una función sobre cada uno de los elementos de un iterador (generalmente una lista o tupla) y retorna un nuevo iterador cuyos elementos son el resultado de dicha operación.
		->Puede ejecutar una función sobre varios iteradores simultáneamente. En ese caso, la función pasada como primer argumento debe esperar tantos parámetros como iteradores se hayan pasado.
		->Ej: define una función dup(n) que retorna el doble de su argumento, y la aplica a cada uno de los elementos de la lista vía map().
			def dup(n):
    			return n * 2
			print(list(map(dup, [1, 2, 3, 4])))

			mult() retorna el producto de sus dos argumentos, y es aplicada por map() a las listas especificadas del siguiente modo: mult(1, 5), mult(2, 5), mult(3, 7), etc.




>>>LAMBDA:  lambda num: num*2     -> recibe num y devuelve num*2

	-> Función anónima (sin nombre). 
    -> Debe tener una única expresión (y no un bloque de acciones)
    -> Para usarla, la guardamos en una variable y la llamamos como a una función normal
    	doblar = lambda num: num*2
    	doblar(2)
    -> Ej1: Comprobar si un número es impar: 
       		impar = lambda num: num%2 != 0
       		impar(5)
    -> Ej2: Dar vuelta una cadena de string
    		revertir = lambda cadena: cadena[::-1]
    		revertir("Hola")
    -> Ej3: Sumar dos números 
    		sumar = lambda x,y: x+y
    		sumar(5,2)
