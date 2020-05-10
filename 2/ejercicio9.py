import random



guessesTaken = 0
print('Hola! Cuál es tu nombre?')
myName = input()
number =  random.randint(1, 50)
print('Bien, ' + myName + ', Estoy pensando en un número entre el 1 y el 50.')



print('Adivina el número: ') # Four spaces in front of "print"
guess = int(input())
guessesTaken = guessesTaken +1

    
while(guess!=number):
    while(guessesTaken<3):
        if guess < number:
            print('Nope. El número que suponés es muy bajo.') # Eight spaces in front of "print"
        elif guess > number:
            print('Nope. El número que suponés es muy alto.')
        print('Adivina el número: ')
        guess = int(input())
        guessesTaken = guessesTaken + 1
        
    print(guessesTaken)
    if(guessesTaken==3):
        if number%2==0:
            print("Pista: El número en el que estoy pensando es par")
        else:
            print("Pista: El número en el que estoy pensando es impar")
    print('Adivina el número: ')
    guess = int(input())
    guessesTaken = guessesTaken + 1


print('Buen trabajo, ' + myName + '! Adivinaste mi número en ' ,guessesTaken, ' intentos!')
        
