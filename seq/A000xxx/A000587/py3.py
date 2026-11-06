L=[];t=-1
while[print(-t)]:t=1;L=[t]+[t:=len(L)*L.pop(0)-t for _ in L*1]
