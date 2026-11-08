from math import*
F=[];P=k=1
while 1:X=P-sum(comb(k,j)*F[j]for j in range(k-1));F=[-e*k for e in F]+[-X,0];P*=k;print(X//gcd(X,P));k+=2
