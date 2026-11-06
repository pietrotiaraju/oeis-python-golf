L=[1]*5;n=0
while[print(L[-5]-L[-4])]:
 n-=5
 for h in 1,1,1,1,0:L+=sum(d*L[n-d-4]**h*sum(L[d::d])for d in range(n,0,5))//n,
