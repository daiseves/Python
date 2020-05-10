def imprimeNombres1(*args):
    aux=0
    for arg in args:
        print("{} : {}".format(aux,arg))
        aux+=1

def imprimeNombres2(*args):
    aux=enumerate(args)
    for arg in aux:
        print (arg)

imprimeNombres1("Lara", "Agustin", "Santiago", "Andrea", "Sofia")
print()
imprimeNombres2("Lara", "Agustin", "Santiago", "Andrea", "Sofia")
        
