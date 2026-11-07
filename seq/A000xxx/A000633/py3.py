m=6
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((8*(V[1]-1)**2-X*((V[1]**2+V[2])**2-2*V[2]**2-2*V[4]))//X**~-m%X>>3);m+=1
