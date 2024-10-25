#7. Sortati o lista de elemente citite de la tastatura, folosind orice metoda de sortare doriti (nu functia sort).

Lista_initiala = [-100, 5, 8, 17, -76, -3, 1000, 99]
Lista_finala = []
while Lista_initiala:
    min = Lista_initiala[0]
    for a in Lista_initiala: 
        if a < min:
            min = a
    Lista_finala.append(min)
    Lista_initiala.remove(min)    

print (Lista_finala)