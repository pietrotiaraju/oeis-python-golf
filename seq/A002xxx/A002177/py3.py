from math import*
n=f=1
while 1:r=range(n+1);M=f*n+f;K=n*len(bin(n));B=1<<K;L=[sum((P>>K*i&B-1)*(M:=-M)//~i for i in r)*comb(n,k)for k in r if[P:=prod(j+n*B for j in r if j-k)]];print(L[0]//gcd(M*f,*L));n+=1;f*=n
