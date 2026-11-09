L=[1]*6;n=0
while[print(L[-6])]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d:2:d])for d in range(n,0,3))//n,
