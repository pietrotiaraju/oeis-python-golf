m=1
while B:=4**m:V=P=[1]*4*m;print((-sum(V[1]*(V[1]-(V:=[1+B**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%B**m//6for k in range(m)]+P)[1])for _ in P)-B//8*((V[1]**2+V[2])**2-2*V[2]**2-2*V[4]))//B**~-m%B);m+=1
