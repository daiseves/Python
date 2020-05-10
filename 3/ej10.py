from functools import reduce

def operacion(operacion, *args, **kargs):
    texto = ""
    if operacion=="+":
        result = sum(args)
    if operacion=="*":
        result = reduce((lambda x,y: x*y), args)
    for key, value in kargs.items():
        texto += key + "= " + value + " /"
        
    print("La operación solicitada fue {}, el resultado es: {} por {}".format(operacion, result, texto))



operacion("*", 3,4,5,7,8, nombre="Art", apellido="Nose", direccion=" Av. Siempre Libre 88")
