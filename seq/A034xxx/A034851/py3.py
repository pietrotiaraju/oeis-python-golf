from math import*
n=k=0
while[print(comb(n,k)+(n|~k)%2*comb(n//2,k//2)>>1)]:k=-~k%-~n;n+=k<1
