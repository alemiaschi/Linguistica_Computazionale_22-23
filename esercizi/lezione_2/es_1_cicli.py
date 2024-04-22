'''Scrivere un programma che, data in input una lista di interi, 
restituisca il totale di numeri pari e dispari presenti al suo interno'''

lista = [4, 5, 3, 12, 9, 11, 7, 21]

pari = 0
dispari = 0
for numero in lista:
    if numero%2 == 0:
        pari+=1
    else:
        dispari+=1

print(pari)
print(dispari)
