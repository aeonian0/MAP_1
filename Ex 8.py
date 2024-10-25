#8. Scrieti un program care afiseaza ziua saptamanii pentru un numar citit de la tastatura (de la 1 la 7) unde  1=luni , 7 = duminica.

ziua = int(input("Introduceti numarul zilei (1-7) : "))

if ziua == 1 :
    print("Luni")

elif ziua == 2 :
    print("Marti")

elif(ziua == 3) :
    print("Miercuri")

elif(ziua == 4) :
    print("Joi")

elif(ziua == 5) :
    print("Vineri")

elif(ziua == 6) :
    print("Sambata")

elif (ziua == 7) :
    print("Duminica")

else :
    print("Va rog introduceti un numar intre 1 si 7")