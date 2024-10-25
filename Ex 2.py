#2.Afisarea primelor 20 de numere impare.

print("Primele 20 de numere impare sunt:")
contor = 0
for nr in range(1, 1000): 
    if nr%2!=0 and contor<20: 
            print(nr) 
            contor +=1