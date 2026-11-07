m=1
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print(2*V[1]*pow(2-X*(V[1]**2+V[2]),-1,X**m)//X**~-m%X);m+=1