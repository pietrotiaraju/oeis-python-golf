from math import comb as C
d=[n:=1]
while[print(sum(C(n,p)*C(n-p,k-~k)*(abs(d[k])+C(p+k-1,p))for k in range(1,n)for p in range(n)))]:d+=n*n-sum(C(n,i)**2*d[i]for i in range(n)),;n+=1
