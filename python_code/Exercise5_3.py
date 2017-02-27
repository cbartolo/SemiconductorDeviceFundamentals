#Exercise_5.3
#Constants requires

import numpy as np
import matplotlib.pyplot as plt

T=300
k=8.617*10**-5
e0=8.85*10**-14
KS=11.8
ni=1*10**10
EG=1.12
q=1.602*10**-19

NB= np.logspace(14,17) #Doping ranges from 1e14 to 1e17
VA=[0.5, 0, -10]

#Depletion Width calculations
"""
VBI=[]
for nb in NB :
    Vbi=EG/2 + k*T*np.log(nb/ni)
    VBI.append(Vbi)
       
print (VBI)
"""
#LIST COMPRENHENSION

VBI=[(EG/2 + k*T*np.log(nb/ni)) for nb in NB]
#print (VBI)


index=0
W=[[],[],[]]

for va in VA:
    for vbi in VBI:
        w=1.0*10**4*np.sqrt(2*KS*e0/q*(vbi-VA[index])/NB[VBI.index(vbi)])
        W[index].append(w)
    index+=1

        
plt.loglog(NB,W[0],NB,W[1], NB,W[2])        
plt.axis([1.0*10**14, 1.0*10**17, 1.0*10**-1, 1.0*10**1])
plt.grid(which='both')
plt.xlabel('NA or ND (cm3)')
plt.ylabel('W (micrometers)')     

##Still is neccesary to write the nottations for each VA used to make clearer the figure