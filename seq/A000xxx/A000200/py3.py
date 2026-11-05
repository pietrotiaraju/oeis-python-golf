m=1
while B:=4**m:V=P=[1]*3*m;print((sum((V[1]-(V:=[1+B**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%B**m//6for k in range(m)]+P)[1])**2for _ in P)+V[2])//B**~-m%B//2);m+=1
