*L,n=1,1,0
while[print(L[-1])]:
 n-=2
 for h in 0,1:L+=sum(d*L[-d*h]*sum(L[d::d])for d in range(n,0,2))//n,
