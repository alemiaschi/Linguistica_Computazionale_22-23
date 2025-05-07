'''Chiedere all’utente di inserire due numeri reali a e b (diversi fra loro)
e stampare il maggiore fra i due'''

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

a = float(a)
b = float(b)

if a == b:
    print("Guarda che i numeri sono uguali")
else:
    if a > b:
        print("Il numero maggiore è: ", a)
    else:
        print("Il numero maggiore è: ", b)
