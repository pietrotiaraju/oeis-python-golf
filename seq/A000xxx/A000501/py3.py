n=0
while 1:
 N=F=1;d=0
 while d<2*n or -N%F<n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print(N//F);n+=1
