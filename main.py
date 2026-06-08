# main.py
import sys
from utilitats import funcio1

x = sys.argv[1] 

print(f"--- Iniciant l'enregistrament al fitxer: {x} ---")
print("Escriu text línia per línia. Per acabar, escriu 'final'.")

llista1 = True
while llista1:
    b = input("> ")
    
    res = funcio1(x, b)
    
    if b == "final":
        llista1 = False

print("Programa finalitzat correctament.")