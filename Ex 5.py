#5. Afisati suma si media unei liste de numere citite de la tastatura.

a = []
n = int(input("Introduceti numarul de elemente: "))
for i in range(0, n):
    elemente = int(input())
    a.append(elemente)
print(a) 
 
avg = sum(a) / len(a)
print('Media numerelor din lista este:', avg)

sum=sum(a)
print('Suma listei de numere este:', int(sum))