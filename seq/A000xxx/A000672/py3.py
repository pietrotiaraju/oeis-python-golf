m=2
while X:=4**m:V=P=[1]*2*m;[V:=[1+X**k*(V[k]**2+V[2*k])%X**m//2for k in range(m)]+P for _ in P];print((3*V[1]-X*X*(V[1]**3-V[3]))//X**~-m%X//3);m+=1