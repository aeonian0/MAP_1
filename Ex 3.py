#3.Cel mai mare divizor comun pentru 2 numere citite de la tastatura.

def CelMaiMareDivizorComun(a,b):
    while a!=b:
        if a>b: a =a-b
        else: b=b-a
    return a
a = int(input('a = '))
b = int(input('b = '))
print('Cel mai mare divizor comun al celor doua numere este =', CelMaiMareDivizorComun(a,b))