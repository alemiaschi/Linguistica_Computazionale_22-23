'''Chiedere all’utente di inserire una stringa e crearne una nuova 
invertendo il primo carattere con l’ultimo'''

stringa = input("Inserisci una stringa: ")

nuova_stringa = stringa[-1] + stringa[1:-1] + stringa[0]

print("La nuova stringa è: ", nuova_stringa)
