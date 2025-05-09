'''
Scrivere un programma in python che, a partire da un testo e usando la libreria nltk/stanza, restituisca in output la Type/Token Ratio (TTR)
'''

import sys
import nltk

def calcolo_token(testo, sent_tokenizer):
    tokensTOT = []
    with open(testo, "r") as f:
        for line in f:
            frasi = sent_tokenizer.tokenize(line)
            for frase in frasi:
                tokens = nltk.word_tokenize(frase)
                tokensTOT+=tokens

    vocabolario = list(set(tokensTOT))

    return tokensTOT, vocabolario

def main(file1):
    sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

    tokensTOT, vocabolario = calcolo_token(file1, sent_tokenizer)

    ttr = len(vocabolario) / len(tokensTOT)

    print("La TTR del documento è", ttr)

main(sys.argv[1])