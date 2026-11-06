L=[1]*4;n=0
while[print(L[-4]-L[-3])]:
 n-=4
 for h in 1,1,1,0:L+=sum(d*L[n-d-3]**h*sum(L[d::d])for d in range(n,0,4))//n,
