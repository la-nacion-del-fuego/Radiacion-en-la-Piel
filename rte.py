#!/usr/bin/env python3

#
#  Radiative Transfer Equation
#  Copyright (C) 2019 Victor De la Luz
#                     vdelaluz@enesmorelia.unam.mx
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import math
import matplotlib.pyplot as plt

c=3e10 #cm/s
kB= 1.38e-16 #[ergK-1]

#opacity [cm-1]
def k(L):
    return 0.244 + (85.3 * math.e**(-(L-154)/66.2))

#optical depth (adimensional)
def tau(dx,x,wl,L):
    return (dx/2.0)*(k(L) + k(L))

N = 100
I0 = 250000 #[erg/cm2 sec cm ster]
nu = 1e8 #Hz
dx = 0.1   #[mm]
wl = c/nu #Amstrongs
lmd = 500

layers = range(1,int(N+1))
X = []
Y = []
I = I0
for i in layers:
    x = float(i)*dx
    I = I*math.exp(-tau(dx,x,wl,lmd))
    X.append(x)
    Y.append(I)

fig,ax = plt.subplots()
fig.suptitle("Absorcion de luz solar en el talon del pie")
ax.plot(X,Y)
ax.set_xlabel("Densidad de la piel mm")
ax.set_ylabel("Intensidad Especifica")

plt.savefig("Ejemplo.jpg", bbox_inches='tight')
plt.show()
