import math
t=[4];E=[-1,N:=1]
while 1:N+=1;E+=(e:=6*E[-1]-E[-2]-t[-1]),;t+=(3*e-E[-2])//N,;print((sum(4*E[math.gcd(k,N)]+t[N-k%2>>1]for k in range(N))+t[-2]-4*e)//8//N)
