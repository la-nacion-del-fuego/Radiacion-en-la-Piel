#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt

c=3e10 #cm/s

#opacity [cm-1]
def k(L):
    return 0.244 + (85.3 * math.e**(-(L-154)/66.2))

#optical depth (adimensional)
def tau(dx,x,wl,L):
    return (dx/2.0)*(k(L-dx) + k(L))

N = 100
Ns = [100,40,1000,200,5]
Names = ["Talon del pie","Parpado","Abdomen Personas Obesas","Abdomen Personas Delgadas","Escroto"]
colorsGraphs = ["Green","Blue","Purple","Red","Brown"]
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

iterator = 0
for x,y in zip(savesX,savesY):
    plt.figure(figsize=(8,5))
    plt.plot(x,y,colorsGraphs[iterator])
    plt.title(Names[iterator])
    plt.xlabel("Densidad de la piel en mm")
    plt.ylabel("Intensidad Especifica")
    plt.savefig("Ejemplo "+ Names[iterator] + ".jpg")
    iterator += 1
    plt.show()
