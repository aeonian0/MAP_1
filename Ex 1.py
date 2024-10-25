#1.Suma numerelor de la 1 la 100.

nr= 1
if nr < 0:
   print("Eroare")
else:
   sum = 0
   while(nr> 0 and nr<=100):
       sum += nr
       nr += 1
   print("Suma numerelor de la 1 la 100 este:", sum)