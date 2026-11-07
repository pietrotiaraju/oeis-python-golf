m=1
while X:=9**m:V=P=[1]*4*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];f=V[1]**2+V[2];print((4*f-X*(f*f-2*V[2]**2-2*V[4]))//X**~-m%X//8);m+=1
