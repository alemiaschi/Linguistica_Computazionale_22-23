import sys

def main():
    file_testo = sys.argv[1]

    # Apertura e lettura del file
    contenuto = open(file_testo, "r", encoding="utf-8")
    frasi = contenuto.readlines()

    parole_testo = []
    for frase in frasi:
        frase1 = frase.rstrip("\n")
        parole = frase1.split(" ")

        parole_testo+=parole

    output = open("output.txt", "w")

    for parola in parole_testo:
        output.write(parola + '\n')

    contenuto.close()
    output.close()

main()