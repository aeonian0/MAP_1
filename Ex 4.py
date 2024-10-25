#4. Afisati daca un numar citit de la tastatura este prim.

print('Introduceti un numar ')
nr = int(input())

if nr > 1:
    for i in range(2,int(nr/2)):
        if(nr%i) == 0:
            print(str(nr) + " nu este numar prim!")
            break
    else:
        print(str(nr) + " este numar prim!")