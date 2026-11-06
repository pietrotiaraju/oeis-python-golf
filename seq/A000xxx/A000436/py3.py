from math import*
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(comb(2*n+0,2*k)*(-9)**k*a[-k]for k in range(1,n+1))];print(a[-1])
