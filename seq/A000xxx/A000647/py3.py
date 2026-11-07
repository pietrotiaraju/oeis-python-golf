m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((V[1]**8+3*V[2]**4)//X**~-m%X//4);m+=1