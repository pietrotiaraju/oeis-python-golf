L=[1]*3;n=0
while[n>-24or print(L[-3]-L[-2]-sum(L[-i-2]*(L[i-2]-L[i-1])for i in range(n,0,3)))]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d::d])for d in range(n,0,3))//n,
