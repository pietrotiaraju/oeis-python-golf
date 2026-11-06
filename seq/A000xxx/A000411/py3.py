from math import*
a=[]
while 1:
 n=len(a);a+=[6*(-9)**n-2*sum(comb(2*n+1,2*k)*(-16)**k*a[-k]for k in range(1,n+1))];print(a[-1])
