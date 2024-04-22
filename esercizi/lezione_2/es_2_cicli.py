'''Scrivere un programma che data in input una lista a contenente n parole, 
restituisca in output un’altra lista b di interi che rappresentano 
la lunghezza delle parole contenute in a'''

a = ["roma", "pisa", "napoli", "viareggio", "catania"]
b = []

for parola in a:
    b.append(len(parola))

print(b)
