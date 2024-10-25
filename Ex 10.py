#10. Rezolvati ecuatia de gradul al doilea.

import math
 
def cuadrica(a, b, c):
    p = b / (2 * a)
    q = (b**2 - 4*a*c) / (4*a)
    radacina1 = p + math.sqrt(q)
    radacina2 = p - math.sqrt(q)
    return radacina1, radacina2
 
a = 6
b = -15
c = 7
radacini = cuadrica(a, b, c)
print("Radacinile sunt:", radacini)