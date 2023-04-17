'''Scrivere un programma che, data in input una frase, crei e stampi una nuova frase 
contenente underscore (“_”) al posto degli spazi (es. “Questo è un esercizio” in “Questo_è_un_esercizio”)'''

frase = "Questo è un esercizio"
nuova_frase = ""

for car in frase:
    if car == " ":
        nuova_frase+="_"
    else:
        nuova_frase+=car

print(nuova_frase)
