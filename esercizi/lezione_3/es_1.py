'''Scrivere un programma che legga un file di testo con la seguente struttura:
Pippo 22
Pluto 34
...
Alessio 29
e memorizzi il suo contenuto all’interno di un dizionario 
(es. {“Pippo”: 22, “Pluto”: 34, “Alessio”: 29})'''

import sys

def main(doc):
    dizionario = {}
    file1 = open(doc, 'r', encoding='utf-8')
    contenuto = file1.readlines()
    for riga in contenuto:
        elementi = riga.rstrip('\n').split(' ')
        numero = int(elementi[1])
        dizionario[elementi[0]] = numero

    file1.close()
    print(dizionario)

main(sys.argv[1])
