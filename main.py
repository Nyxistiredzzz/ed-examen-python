# main.py
import sys
from utilitats import escriure_linia

try:
    nom_fitxer = sys.argv[1]
except IndexError:
    print("Error: Has d'especificar el nom del fitxer per consola.")
    sys.exit(1)

print(f"--- Iniciant l'enregistrament al fitxer: {nom_fitxer} ---")
print("Escriu text línia per línia. Per acabar, escriu 'final'.")

try:
    bucle_actiu = True
    while bucle_actiu:
        paraula_usuari = input("> ")

        if paraula_usuari == "final":
            bucle_actiu = False
        else:
            resultat = escriure_linia(nom_fitxer, paraula_usuari)

except (FileNotFoundError, PermissionError) as error:
    print(f"Error en accedir al fitxer: {error}")
    sys.exit(1)

print("Programa finalitzat correctament.")
