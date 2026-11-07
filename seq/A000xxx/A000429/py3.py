L=[1]*8;n=0
while[print(L[-8]-L[-7])]:n-=8;exec("L+=sum(d*L[n-d-7]*sum(L[d::d])for d in range(n,0,8))//n,;"*7);L+=1,