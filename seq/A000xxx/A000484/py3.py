n=0;S=1
while 1:
 S*=2;K=S.bit_length();E=20*-~K
 p=sum((-1)**k*S*a//((2*k+1)*b**(2*k+1))for a,b in((16,5),(-4,239))for k in range(K))
 while p>E and(q:=3*n*S//(p+E))==3*n*S//(p-E):print((1,0,-1,-1,0,1)[q%6]);n+=1
