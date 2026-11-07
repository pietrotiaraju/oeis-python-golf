L=[1]*7;n=0
while[print(L[-7]-L[-6])]:
 n-=7
 for h in[1]*6+[0]:L+=sum(d*L[n-d-6]**h*sum(L[d::d])for d in range(n,0,7))//n,