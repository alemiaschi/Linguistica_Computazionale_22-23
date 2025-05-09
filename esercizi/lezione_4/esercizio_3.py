'''
Scrivere un programma in python che, a partire da un testo e usando la libreria nltk/stanza, 
estragga il nome e il verbo (lunghi almeno 4 caratteri) con frequenza massima
'''

import sys
import stanza

def estrazione_nome_verbo(testo, nlp):
    fileInput  = open(testo, "r", encoding="utf-8")
    raw = fileInput.read()

    doc = nlp(raw)

    verbi = []
    sostantivi = []

    for sent in doc.sentences:
        for word in sent.words:
            if len(word.text) >= 4 and word.upos == "NOUN":
                sostantivi.append(word.text)
            elif len(word.text) >= 4 and word.upos == "VERB":
                verbi.append(word.text)

    verbi_set = list(set(verbi))
    sostantivi_set = list(set(sostantivi))

    verbo_piu_frequente = ""
    frequenza_max_verbo = 0
    for verbo in verbi_set:
        frequenza = verbi.count(verbo)
        if frequenza > frequenza_max_verbo:
            frequenza_max_verbo = frequenza
            verbo_piu_frequente = verbo

    sostantivo_piu_frequente = ""
    frequenza_max_sostantivo = 0
    for sostantivo in sostantivi_set:
        frequenza = sostantivi.count(sostantivo)
        if frequenza > frequenza_max_sostantivo:
            frequenza_max_sostantivo = frequenza
            sostantivo_piu_frequente = sostantivo

    return verbo_piu_frequente, frequenza_max_verbo, sostantivo_piu_frequente, frequenza_max_sostantivo

def main(file1):
    nlp = stanza.Pipeline(lang="en", processors="tokenize,pos")

    verbo_piu_frequente, frequenza_max_verbo, sostantivo_piu_frequente, frequenza_max_sostantivo = estrazione_nome_verbo(file1, nlp)

    print("Il verbo più frequente è:", verbo_piu_frequente, " con frequenza:", frequenza_max_verbo)
    print("Il sostantivo più frequente è:", sostantivo_piu_frequente, " con frequenza:", frequenza_max_sostantivo)

main(sys.argv[1])