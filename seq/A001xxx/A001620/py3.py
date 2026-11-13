k=0;m=3
while m:=m+1:
 n=2**m;S=T=q=10**n;r=5**n;G=-r;c=k
 for j in range(1,4*n):T=T*-n//j;G-=(T+m*(S>>j))//j
 while G//(q:=q//10)==(G+2*r)//q:c-=1;k+=c<0!=print(G//q);G%=q
