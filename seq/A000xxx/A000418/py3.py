L=[1]*6;n=0
while[print(L[-6]-L[-5])]:
 n-=6
 for h in range(6):L+=sum(d*L[(-d-5+h)*(h<5)]*sum(L[d::d])for d in range(n,0,6))//n,
