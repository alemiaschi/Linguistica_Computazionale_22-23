'''Scrivere un programma che prende in input un dizionario con la seguente struttura: 
{“Nome dello studente”: “lista dei voti”, ecc} (es. {“Alessio”: [21, 28, 30, 18], “Laura”: [21, 20, 30, 30, 28, 25]}). 
Per ogni studente:
- verificare se nel suo libretto sono presenti almeno 5 valutazioni
- In caso positivo, stampare il nome dello studente e la media delle sue valutazioni
- In caso negativo, stampare “Lo studente X non ha raggiunto il numero minimo di esami. Numeri di esami mancanti: n”,
dove n corrisponde al numero di esami mancanti per arrivare a 5
'''

diz = {"Alessio": [21, 28, 30, 18],
       "Laura": [21, 20, 30, 30, 28, 25]}

for k, v in diz.items():
    if len(v) < 5:
        esami_mancanti = 5 - len(v)
        print("Lo studente", k, "non ha raggiunto il numero minimo di esami. Numero di esami mancati:",
              esami_mancanti)
    else:
        media = 0.0
        for voto in v:
            media+=voto
        media = media / len(v)
        print(k, media)
