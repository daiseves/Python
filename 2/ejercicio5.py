lista=[]

print("""1: ingresar números
2: ordenar números
3: calcular el máximo
4: calcular el mínimo
5: calcular el promedio
0: para terminar""")


num=int(input('Ingrese la opción:'))
while(num!=0):
    if(num==1):
        num=int(input('Ingrese numero para agregar:'))
        lista.append(num)
        print(lista)
    elif (num==2):
        lista.sort()
        print(lista)
    elif(num==3):
        num_max=max(lista)
        print("Número máximo de la lista: ",num_max)
    elif(num==4):
        num_min=min(lista)
        print("Número mínimo de la lista: ",num_min)
    elif(num==5):
        suma=sum(lista)
        promedio=suma/len(lista)
        print("Promedio de los valores de la lista: ",promedio)
    num=int(input('Ingrese la opción:'))
print("Programa terminado")
        
             

