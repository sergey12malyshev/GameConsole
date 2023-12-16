#

import math

R2 = 94000 #ohm
Vout = 3.4
Vfb = 0.500
 
R1 =  R2 * (Vout/Vfb - 1)

print(R1)