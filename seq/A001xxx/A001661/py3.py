n=1
while 1:
 n+=1;S=k=1;X=16<<n*n
 while~S>>(P:=k**n)&(1<<P)-1:r=X<2*P;X<<=r;S|=S<<P&(1<<X)-1;S**=r<1;k+=1-k*r
 print(len(bin(~S&(1<<P)-1))-3)
