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

#opacity [cm-1]
def k(L):
    return 0.244 + (85.3 * math.e**(-(L-154)/66.2))

#optical depth (adimensional)
def tau(dx,x,wl,L):
    return (dx/2.0)*(k(L) + k(L))

N = 100
Ns = [100,40,1000,200]
Names = ["Talon del pie","Parpado","Abdomen Personas Obesas","Abdomen Personas Delgadas"]
colorsGraphs = ["Green","Blue","Purple","Red"]
I0 = 250000 #[erg/cm2 sec cm ster]
nu = 1e8 #Hz
dx = 0.1   #[mm]
wl = c/nu #Amstrongs
lmd = 500

savesX = []
savesY = []
savesNames = []

for n,j in zip(Names,Ns):
    X = []
    Y = []
    I = I0
    for i in range(1,j+1):
        x = float(i)*dx
        I = I*math.exp(-tau(dx,x,wl,lmd))
        X.append(x)
        Y.append(I)
    savesX.append(X)
    savesY.append(Y)
    savesNames.append(n)

fig,ax = plt.subplots(2,2)
fig.suptitle("Absorcion de la luz en diferentes partes del cuerpo")
fig.set_size_inches(13,10,forward=True)
iterator = 0
for y in range(2):
    for x in range(2):
        ax[y][x].plot(savesX[x+y],savesY[x+y],colorsGraphs[iterator])
        ax[y][x].set_title(Names[iterator])
        iterator += 1

for ax in ax.flat:
    ax.set(xlabel='Densidad de la piel en mm', ylabel='Intensidad Especifica')

plt.savefig("Ejemplo.jpg")
plt.show()