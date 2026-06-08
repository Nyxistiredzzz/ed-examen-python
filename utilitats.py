# utilitats.py

def escriure_linia(nom_fitxer, contingut):
    f = open(nom_fitxer, "a", encoding="utf-8")
    f.write(contingut + "\n")
    f.close()
    return True
