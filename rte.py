#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt

c=3e10 #cm/s

#opacity [cm-1]
def k(L,initLayer,finalLayer,x):
    if finalLayer >= x >= initLayer:
        return 0.244 + (85.3 * math.e**(-(L-154)/66.2))
    else:
        return 0

#N = 100
Ns = [10,4,100,20,5,3]
Names = ["Talon del pie","Parpado","Abdomen Personas Obesas","Abdomen Personas Delgadas","Escroto","Gluteos"]
colorsGraphs = ["Green","Blue","Purple","Red","Brown","Gold"]
I0 = 250000 #[erg/cm2 sec cm ster]
nu = 1e8 #Hz
dx = 0.1   #[mm]
wl = c/nu #Amstrongs
lmd = 500


savesX = []
savesY = []
savesNames = []

for n,i in zip(Names,Ns):
    X = []
    Y = []
    for x in range(i+int(i*.5)):
        opacity = k(lmd,i*.5,i,x)
        X.append(x)
        Y.append(opacity)
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