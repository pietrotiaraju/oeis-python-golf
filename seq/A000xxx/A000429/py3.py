L=[1]*7;n=0
while[print(L[-7]-L[-6])]:
 n-=7
 for h in range(7):L+=sum(d*L[(-d-6+h)*(h<6)]*sum(L[d::d])for d in range(n,0,7))//n,
