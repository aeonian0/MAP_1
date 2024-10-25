#6. Se citesc 3 numere de la tastatura, verificati daca acestea pot reprezenta unghiurile unui triunghi.

a = int(input())
b = int(input())
c = int(input())
def EsteTriunghi(a, b, c):
   if a != 0 and b != 0 and c != 0 and (a + b + c) == 180:
      if (a + b)>= c or (b + c)>= a or (a + c)>= b:
         return print('Este triunghi')
   else:
      return print('Nu este triunghi')
   
print(EsteTriunghi(a, b, c))