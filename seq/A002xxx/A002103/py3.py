n=0
while 1:
 X=8<<5*n;N=X**n;B=A=k=0;m=4*n+1
 while k*k<=n:B+=2*X**(k*k);A+=X**(k*k+k);k+=1
 print((pow(B-1,m,N*X)*pow(A,-m,N*X)+N//2)//N%X//m);n+=1
