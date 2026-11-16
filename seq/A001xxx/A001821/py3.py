L=[p:=1]*4;m=3
while[print(p)]:p=0;m-=3;L=[p:=p+(m:=m+1)**2*x for x in L]
