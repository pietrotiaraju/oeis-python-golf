n=0;S=1
while 1:
 S*=2;K=S.bit_length();E=20*K+20
 p=sum((-1)**k*S*16//((2*k+1)*5**(2*k+1))-(-1)**k*S*4//((2*k+1)*239**(2*k+1))for k in range(K))
 while p>E and(q:=6*n*S//(p+E))==6*n*S//(p-E):print((0,1,1,1,1,0,0,-1,-1,-1,-1,0)[q%12]);n+=1
