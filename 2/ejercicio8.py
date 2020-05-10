cadena = input("Escriba un string: ")
cadena = cadena.replace(' ', '')
 
d = dict()
 
for caracter in cadena:
    if caracter not in d:
        d[caracter] = 1
    else:
        d[caracter] = d[caracter] + 1
print (d)
print(len(d))

def es_primo(num):
    if num<2:
        return False
    elif num==2:
        return True
    elif num > 2:     
        for divisor in range(2, num):  
            if num % divisor == 0:
                return False
            elif num%divisor!=0 and divisor == num-1:
                return True 


for i, elem in d.items():
    if es_primo(elem) == True:
        print ("La cantidad de veces que aparece la letra ",i," SI es un número primo.")                 
    elif es_primo(elem)== False:
        print("La cantidad de veces que aparece la letra ",i," NO es un número primo.")
    
