n=1
while 1:
 N=F=1;k=0
 while -n*N%F<2*n:k+=1;N=N*k+1;F*=k
 print(n+n*N//F);n+=1
