def sumaTotal(*args):
    suma=sum(args)
    print("La suma de los números {} es: {}".format(args, suma))
 
def strings(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=",kwargs[kwarg])
    

print("Inciso A")
sumaTotal(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

print("Inciso B")
strings(Nombre="Lara", Apellido="Remorini", Sexo="Femenino")


