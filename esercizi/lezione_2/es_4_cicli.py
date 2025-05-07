'''Scrivere un programma che prende in input una stringa e che stampa 
la versione inversa della stessa stringa (es, “ciao” diventerà “oaic”)'''

stringa = "Alessio"
nuova_stringa = ""

lunghezza = len(stringa)-1

while lunghezza >= 0:
    nuova_stringa+=stringa[lunghezza]
    lunghezza-=1

print(nuova_stringa)
