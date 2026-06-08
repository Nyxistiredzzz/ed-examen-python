# utilitats.py

def funcio1(a, b):
    f = open(a, "a", encoding="utf-8")
    f.write(b + "\n")
    f.close()
    return True