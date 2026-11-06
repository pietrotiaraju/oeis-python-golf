n=0
while 1:
 N=n;F=d=1
 while -N%F<n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print(N//F);n+=1
