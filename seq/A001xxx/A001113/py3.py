N=2;F=Q=m=1
while-N%F<=Q or[print(N//F),N:=N%F*10,Q:=Q*10]:m+=1;N=N*m+Q;F*=m
