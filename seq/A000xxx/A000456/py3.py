import math
L=[[1],[1]];n=0
while 1:
 n+=1
 for q,a in enumerate(L,5):a+=[sum(math.comb(n,k)*((k%q==1)-(k%q<1))*a[-k]for k in range(1,n+1))]
 print(L[1][-1]-L[0][-1])
