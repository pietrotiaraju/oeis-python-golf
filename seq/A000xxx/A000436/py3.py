import math
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(math.comb(2*n,2*k)*(-9)**k*a[-k]for k in range(1,n+1))];print(a[-1])
