'''Scrivere un programma che prende in input due liste di interi a e b e restituisce una nuova lista c
contenente le somme dei valori delle due liste. Es. se a = [1,2,3,4,5] e b = [5,6,7,8,9], allora c = [6, 8,
10, 12, 14]. Se le due liste hanno lunghezza diversa, il programma deve stampare il messaggio di
errore “Errore! Le due liste hanno lunghezza diversa!” In ogni caso, l’operazione si deve
interrompere se la nuova lista c raggiunge una lunghezza maggiore di 5 elementi'''

a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 11]

nuova_lista = []
if len(a) != len(b):
    print("Le due liste hanno lunghezza diversa")
else:
    i = 0
    while i < len(a):
        if i == 5:
            break
        somma = a[i] + b[i]
        nuova_lista.append(somma)
        i+=1

    print(nuova_lista)
