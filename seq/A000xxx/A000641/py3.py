m=1
while X:=9**m:M=X**m;V=P=[1]*6*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6for k in range(m)]+P for _ in P];s,t,u=[2*pow(2-X**k*(V[k]**2+V[2*k]),-1,M)for k in(1,2,3)];print(X*V[1]*(s**3+3*s*t+2*u)%M*X//M//6);m+=1
