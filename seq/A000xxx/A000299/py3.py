*L,n=1,1,1,0
while[print(L[-3]-L[-2])]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d::d])for d in range(n,0,3))//n,
