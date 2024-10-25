#9. Afisati maximul dintr-un vector de elemente citit de la tastatura.

def CelMaiMareNumar(a, n):
    x = max(a)
    return x

a = []
n = int(input("Introduceti numarul de elemente: "))
for i in range(0, n):
    elemente = int(input())
    a.append(elemente)
    n = len(a)
print(a)
print ("Cel mai mare numar din vector este: ", CelMaiMareNumar(a, n))