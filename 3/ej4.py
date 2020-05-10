anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5}

n=anim.items()
l=list(n)

for elem in range(len(l)):
    print("")
    print(l[elem][0])
    clave=l[elem][0]
    for i in range(len(clave)):
        pos=l[elem][1]
        
        if i!=pos:
            print('_ ', end="")
        else:
            print(clave[i], end="") 
