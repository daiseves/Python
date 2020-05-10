lista=[]
print("""1: ingresar números
2: Sumar
3: Restar
4: Multiplicar
5: Dividir
0: Terminar""")

op=int(input('Ingrese la opción: '))
while(op!=0):
    if(op==1):
        num1=int(input('Ingrese primer número: '))
        lista.append(num1)
        num2=int(input('Ingrese primer número: '))
        lista.append(num2)
    if (largo==2):
        if(op==2):
            suma=num1+num2
            print("La suma de los dos números es: ",suma)
        elif(op==3):
            resta=num1-num2
            print("La resta de los dos números es: ",resta)
        elif(op==4):
            mult=num1*num2
            print("La multiplicación de los dos números es: ",mult)
        elif(op==5):
            div=num1/num2
            print("La división de los dos números es: ",div)
    elif (largo==0):
        print("No ingresó ningún número para operar")
    op=int(input('Ingrese la opción:'))
 
print("Programa terminado")
    
