L=[1]*8;n=0
while[print(L[-8])]:
 n-=4
 for h in 1,1,1,0:L+=sum(d*L[n-d-3]**h*sum(L[d:3:d])for d in range(n,0,4))//n,
