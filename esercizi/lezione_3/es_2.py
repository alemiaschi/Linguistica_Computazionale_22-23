'''Scrivere un programma che legga un file di testo contenente un nome per riga e
scriva all’interno di un nuovo file i nomi e la loro rispettiva lunghezza in termini di
caratteri. Ad esempio, dato il file:
Alessio
Pippo
Pluto
Ciao
il file di output dovrà presentare la seguente struttura:
Alessio, lunghezza = 7
Pippo,lunghezza = 5
Pluto, lunghezza = 5
Ciao, lunghezza = 4'''

import sys

def main(doc):
    file1 = open(doc, 'r', encoding='utf-8')
    out = open('output.txt', 'w', encoding='utf-8')
    contenuto = file1.readlines()
    for riga in contenuto:
        parola = riga.rstrip('\n')
        stringa = parola + ', lunghezza=' + str(len(parola)) + '\n'
        out.write(stringa)

    file1.close()
    out.close()

main(sys.argv[1])
