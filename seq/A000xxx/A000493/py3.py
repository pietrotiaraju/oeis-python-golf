n=0;S=1
while 1:
 S*=2;K=S.bit_length();E=20*-~K
 p=sum((-1)**k*S*a//((2*k+1)*b**(2*k+1))for a,b in((16,5),(-4,239))for k in range(K))
 while p>E and(q:=n*S//(p+E))==n*S//(p-E):print(-(q%2));n+=1
