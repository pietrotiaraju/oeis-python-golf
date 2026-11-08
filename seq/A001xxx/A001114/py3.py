N=2;F=Q=m=1;b=p=0
while-N%F<=Q or[c:=N//F,N:=N%F*10,Q:=Q*10,c*(b>p)and[print(p:=b),b:=0],b:=b*10+c]:m+=1;N=N*m+Q;F*=m
