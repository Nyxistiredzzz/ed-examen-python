# main.py
import sys
from utilitats import escriure_linia

nom_fitxer = sys.argv[1]

print(f"--- Iniciant l'enregistrament al fitxer: {nom_fitxer} ---")
print("Escriu text línia per línia. Per acabar, escriu 'final'.")

bucle_actiu = True
while bucle_actiu:
    paraula_usuari = input("> ")

    resultat = escriure_linia(nom_fitxer, paraula_usuari)

    if paraula_usuari == "final":
        bucle_actiu = False

print("Programa finalitzat correctament.")
