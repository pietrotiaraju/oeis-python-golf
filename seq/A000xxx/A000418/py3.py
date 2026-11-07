L=[1]*8;n=0
while[print(L[-2]-L[-3])]:n-=7;exec('L+=sum(d*L[n-d-8]*sum(L[d::d])for d in range(n,0,7))//n,;'*6);L+=1,
