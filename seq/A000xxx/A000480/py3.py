n=0
while 1:
 N=F=1;d=0
 while N%F<n**-d:d-=2;N=n**-d+N*~d*d;F*=~d*d
 print(N//F);n+=1
