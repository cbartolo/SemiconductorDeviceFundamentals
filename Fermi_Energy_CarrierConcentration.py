#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:37:57 2017

@author: cesarbartolo
"""



import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp


def charge_neutrality(Ef,T, Na, Nd):
    """Charge neutrality gives the total charge in a semiconductor for different Fermi energy (Ef), Temperature (T)
    Na: concentration of donors and Na: concentration of acceptors"""
    #Na=10**10
    #Nd=10**10
    q=1.602*10**-19 #charge
    m0=9.10938356*10**-31 #kg
    mp=0.81*m0
    mn=1.08*m0
    h=6.626070040 *10**-34  #J.s
    k=1.38064852*10**-23 #J/K
    
    Eg=1.12 #Energy bandgap eV assumed constant but it can be deppendent of temperature
    Ev=0    #Top of the valence band
    Ec=Ev+Eg #Bottom of the conduction band
    
    Ed=Ec-0.044   #Activation energy of donor
    Ea=Ev+0.044   #Activation energy of acceptor
    Nv=2*(2*np.pi*mp*k*T/(h**2))**(3/2)  * 1*10**-6  #cm-3  #Effective density of states of valence band
    Nc=12*(2*np.pi*mn*k*T/(h**2))**(3/2)  * 1*10**-6  #cm-3 #Effective density of states of conduction band
    Ni=np.sqrt(Nc*Nv)*np.exp(-(Eg*q)/(2*k*T))   #Intrinsic concentration (function of T)
    Ei=((Ec+Ev)/2)+(((k*T)/2)*np.log(Nv/Nc))     #Fermi energy of intrinsic level
    n=Nc*np.exp(-(Ec-Ef)*q/(k*T))     #carrier concentration n
    p=Nv*np.exp(-(Ef-Ev)*q/(k*T))      #carrier concentration p

    ###INCOMPLETE IONIZATION ASSUMPTION
    Na_minus=Na/(1+(4*(np.exp(Ef-Ed)*q)/(k*T)))   #Acceptors impurities ionized
    Nd_plus=Nd/(1+(2*(np.exp(Ea-Ef)*q)/(k*T)))    #Donor imporituies ionized
   
      
    return (n+Na_minus-p-Nd_plus)#, Ni, Ei, Nc, Nv, p , n)


#############333
"""
Calculating the Fermi Energy in a range of temperature
"""

Fermi_Level=[]
Temperature=range(50,900)
for T in Temperature:
    #brentq (fucntion, low_limit, high_limit, arguments in function)
    #brentq is used for obtain the fermi energy that makes the charge neutrality function=0
    fermi=sp.brentq(charge_neutrality,0,1.2, args=(T, 10**10,10**15)) #args(Ef, T, Na, Nd)
    Fermi_Level.append(fermi)
    
    
plt.plot( Temperature, Fermi_Level, lw=2)
plt.grid(True)
plt.xlabel('Temperature (K)')
plt.ylabel('Fermi Energy (Ef)')
plt.title('Fermi Energy for Nd>Na')
plt.savefig('Nd=Na.png', dpi=1000)
plt.show




