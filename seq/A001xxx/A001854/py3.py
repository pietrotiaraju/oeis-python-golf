from math import*
T=[P:=[1]];n=1
while[print(n*sum(P[-1]-L[-1]for L in T))]:
 T+=P[:],;P=n*[0]
 for L in T:L+=sum(comb(n-1,j)*-~j*P[j]*L[~j]for j in range(n)),;P=L
 n+=1
