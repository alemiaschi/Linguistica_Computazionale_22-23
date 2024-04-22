'''Data la lista di numeri interi [5, 6, 8, 10, 12] e un numero intero a (da chiedere in input), 
verificare se il primo elemento della lista corrisponde ad a. 
In caso negativo, stampare il primo elemento della lista'''

lista = [5, 6, 8, 10, 12]
num = input("Inserisci un numero: ")

num = int(num)

if lista[0] == num:
    print("Il primo numero della lista corrisponde al numero inserito!")
else:
    print("I due numeri non corrispondono. Il primo numero della lista è: ", lista[0])
