P=[];d=0;u=v=s=1
while[print(s)]:k=d;d+=1;u,v=v,-v-2*k*u;P=[s:=v]+[s:=s+d*(k:=k-1)*p for p in P]
