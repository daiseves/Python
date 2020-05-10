import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic={}
i=5

while(len(colores)!=0):
    num=random.randrange(i)
    clave=colores[num]
    valor=coordenadas[num]
    dic[clave]=valor
    colores.pop(num)
    coordenadas.pop(num)
    i=i-1
    
print(dic)


for elem in dic:
    if elem =='azul':
        valores=dic.get('azul')
        num1=valores[0]
        num2=valores[1]
        sumar = lambda num1,num2: num1+num2
        print (num1,"+",num2, " = ",sumar(num1,num2))
    elif elem=='amarillo':
        valores=dic.get('amarillo')
        num1=valores[0]
        num2=valores[1]
        restar = lambda num1,num2: num1-num2
        print (num1,"-",num2, " = ",restar(num1,num2))
    elif elem=='rojo':
        valores=dic.get('rojo')
        num1=valores[0]
        num2=valores[1]
        dividir  = lambda num1,num2: num1/num2
        print (num1,"/",num2, " = ",dividir(num1,num2))
    elif elem=='rojo':
        valores=dic.get('rojo')
        num1=valores[0]
        num2=valores[1]
        dividir  = lambda num1,num2: num1/num2
        print (num1,"/",num2, " = ",(num1,num2))
    elif elem=='blanco':
        valores=dic.get('blanco')
        num1=valores[0]
        num2=valores[1]
        multiplicar  = lambda num1,num2: num1*num2
        print (num1,"*",num2, " = ",multiplicar(num1,num2))
    elif elem=='negro':
        print("es negro")
            
            
