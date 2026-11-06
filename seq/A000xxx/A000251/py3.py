n=7
while n:=n+1:
 P=S=b=B=4**n;M=B**n
 while b<M:S*=pow(q:=pow(1-b,-1,M),P//b%B,M);P*=q;b*=B
 print((S-P*(P-M//~-B+2))*B//M%B)
