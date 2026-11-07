m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+2*V[3*k])%X**m//3for k in range(m)]+P for _ in P];c=V[1]**2;w=V[2];print((c+w)*(2-X*(c-w))//X**~-m%X//4);m+=1
