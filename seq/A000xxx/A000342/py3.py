L=[1]*5;n=0
while[print(L[-5]-L[-4])]:n-=5;exec("L+=sum(d*L[n-d-4]*sum(L[d::d])for d in range(n,0,5))//n,;"*4);L+=1,