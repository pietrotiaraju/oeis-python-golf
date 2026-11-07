m=2
while X:=8**m:V=U=P=[1]*3*m;R=range(m);[(V:=[1+X**k*(V[k]**3+2*V[3*k])%X**m//3for k in R]+P,U:=[1+X**k*U[k]*U[2*k]%X**m for k in R]+P)for _ in P];c=V[1]**2;w=V[2];print(((c+w)*(2-X*(c-w))-2*(U[1]+U[2]+X*U[4]))//X**~-m%X//4);m+=1
