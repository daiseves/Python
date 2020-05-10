imagenes=['im1','im2','im3']
dic={}

indice=0
for i in imagenes:
    print("Ingrese la  primer coordenada del elemento" " '",imagenes[indice],"'")
    primer=int(input())
    print("Ingrese la segunda coordenada del elemento" " '",imagenes[indice],"'")
    segundo=int(input())
    tupla=(primer, segundo)
    if not dic:
        dic[i]=tupla
    else:
        if tupla in dic.values():
            while tupla in dic.values():
                print("La coordenada ya existe, ingrese una nueva")
                print("Ingrese la  primer coordenada del elemento" " '",imagenes[indice],"'")
                primer=int(input())
                print("Ingrese la segunda coordenada del elemento" " '",imagenes[indice],"'")
                segundo=int(input())
                tupla=(primer, segundo)
            dic[i]=tupla
        else:
            dic[i]=tupla
            
    print(dic)
    indice=indice+1
