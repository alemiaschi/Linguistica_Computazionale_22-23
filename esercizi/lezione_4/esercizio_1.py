'''
Scrivere un programma in python che, a partire da un testo e usando la libreria nltk/stanza, estragga il numero totale di frasi presenti al suo interno 
e calcoli la lunghezza media delle parole (in termini di caratteri)
'''

import sys
import nltk

def calcolo_lunghezza(testo, sent_tokenizer):
    lunghezze_tokens = []
    conteggioFrasi = 0
    with open(testo, "r") as f:
        for line in f:
            frasi = sent_tokenizer.tokenize(line)
            for frase in frasi:
                conteggioFrasi += 1
                tokens = nltk.word_tokenize(frase)
                for token in tokens:
                    lunghezze_tokens.append(len(token))

    media_lunghezza_tokens = sum(lunghezze_tokens) / len(lunghezze_tokens)

    return conteggioFrasi, media_lunghezza_tokens

def main(file1):
    sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

    conteggioFrasi, media_lunghezza_tokens = calcolo_lunghezza(file1, sent_tokenizer)

    print("Il numero totale di frasi è", conteggioFrasi)
    print("La lunghezza media delle parole (in termini di caratteri) è", media_lunghezza_tokens)

main(sys.argv[1])