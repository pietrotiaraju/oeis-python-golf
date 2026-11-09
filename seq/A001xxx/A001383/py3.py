L=[1]*4;n=0
while[print(L[-4])]:
 n-=2
 for h in 1,0:L+=sum(d*L[1-d*h]*sum(L[d:1:d])for d in range(n,0,2))//n,
