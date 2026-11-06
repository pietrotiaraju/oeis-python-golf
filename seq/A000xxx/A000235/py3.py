*L,n=1,1,0
while[print(L[-2]-L[-1])]:
 n-=2
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
