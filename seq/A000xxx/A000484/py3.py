n=0
while 1:
 N=3;F=p=2;d=0
 while N%F<p:d-=2;p*=n*n;N=p+N*~d*d;F*=~d*d
 print(N//F);n+=1
