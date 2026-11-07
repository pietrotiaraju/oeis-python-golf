m=1
while X:=4**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**2+V[2*k])%X**m//2for k in range(m)]+P for _ in P];print(X*(V[1]**3+3*V[1]*V[2]+2*V[3])//X**~-m%X//6);m+=1