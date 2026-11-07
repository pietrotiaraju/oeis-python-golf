L=[c:=1]*4;m=2
while[print(L[-1]-L[-2])]:
 m+=1
 for q in 3,4:L+=sum((c:=c*(m-k)//k)*(-1,1,0,0)[k%q]*L[-2*k]for k in range(1,m)),
