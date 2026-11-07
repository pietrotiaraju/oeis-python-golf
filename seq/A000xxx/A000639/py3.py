m=2
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((V[1]**6+4*V[2]**3+2*V[3]**2+3*(V[1]*V[2])**2+2*V[6])*X**7//X**m%X//12);m+=1
