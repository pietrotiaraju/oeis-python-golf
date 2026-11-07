m=1
while B:=4**m:V=P=[1]*2*m;print((sum((V[1]-(V:=[1+B**k*(V[k]**2+V[2*k])%B**m//2for k in range(m)]+P)[1])**2for _ in P)+V[2])//B**~-m%B//2);m+=1