# utilitats.py

def escriure_linia(nom_fitxer, contingut):
    with open(nom_fitxer, "a", encoding="utf-8") as fitxer:
        fitxer.write(contingut + "\n")
    return True
