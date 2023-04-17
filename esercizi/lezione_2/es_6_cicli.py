'''Scrivere un programma che, data in input una lista di interi, 
stampi i numeri divisibili per 5. Se scorrendo la lista si 
trova un numero maggiore o uguale di 150, interrompere il ciclo'''

lista = [10, 15, 34, 33, 76, 150, 50, 10]

for numero in lista:
    if numero >= 150:
        break
    if numero%5 == 0:
        print(numero)
