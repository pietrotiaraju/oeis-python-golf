n=0
while 1:
 p=2*n;N=p+1;F=2;d=0
 while N%F<p:d+=2;p*=n*n;N=p+N*~d*d;F*=~d*d
 print(N//F);n+=1
