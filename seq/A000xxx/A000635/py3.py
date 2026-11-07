m=1
while X:=9**m:M=X**m;V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6for k in range(m)]+P for _ in P];print((2*pow(2-X*(V[1]**2+V[2]),-1,M)-1)%M*X//M);m+=1
