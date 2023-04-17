'''Chiedere all’utente di inserire un numero intero e verificare 
se tale numero è pari'''

numero = input("Inserisci un numero: ")
numero = int(numero)

risultato = numero%2
print(risultato == 0)
