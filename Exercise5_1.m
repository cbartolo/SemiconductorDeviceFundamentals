%Exercise 5_1
%matlab script
%Computation of Vbi (p+/n and n+/p junctions)

%Definition of constants
Eg=1.12 ; %silicon
kT=0.0259; %eV
ni=1.0e10 ; % cm-3

ND= logspace(14,17);
Vbi=Eg/2 + kT.*log(ND./ni);

%plotting results
close
semilogx(ND,Vbi); grid
axis([1.0e14 1.0e17 0.75 1])
xlabel('NA or ND (cm-3)');ylabel('Vbi (volts)')
text(1e16,0.8, 'Si, 300K')
text(1e16,0.78, 'p+/n and n+/p diodes');

