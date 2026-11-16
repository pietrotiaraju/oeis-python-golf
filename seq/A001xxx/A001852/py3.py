from math import*
T=[P:=[0,1]];s=v=2;N=1
while[print(N*v-s+v//2-P[-1])]:
 N+=1;T+=P[:],;P=N*[0];s=0
 for L in T:g=[comb(N,k)*P[k]*L[-k]for k in range(N)];L+=sum(map(int.__mul__,g,range(N)))//~-N,;s+=(v:=2*L[-1]-sum(g));P=L
