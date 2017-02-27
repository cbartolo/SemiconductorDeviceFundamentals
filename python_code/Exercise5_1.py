# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 06:54:45 2017

@author: cesarbartolo
"""
import numpy as np
import matplotlib.pyplot as plt



Eg=1.12  #silicon
kT=0.0259 #eV
ni=1.0e10  # cm-3

#ND= logspace(14,17);
ND=np.logspace(14,17)
VBI=[]

for nd in ND:
    Vbi= (Eg/2) + kT*np.log(nd/ni)
    VBI.append(Vbi)

#plotting results

plt.semilogx(ND,VBI)
plt.grid(True)
plt.xlabel('NA or ND (cm-3)')
plt.ylabel('Vbi (volts)')
plt.axis([10**14, 10**17, 0.75, 1])
plt.annotate('Si, 300K', xy=(10**16,0.8))
plt.annotate('p+/n and n+/p diodes', xy=(10**16,0.78))
