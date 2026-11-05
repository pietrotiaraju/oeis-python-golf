r=[n:=0,1]
while[print(r[-n])]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
