m=1
while B:=4**m:V=P=[1]*3*m;print((3-3*sum(V[1]*(V[1]-(V:=[1+B**k*(V[k]**2+V[2*k])%B**m//2for k in range(m)]+P)[1])for _ in P)+B*(V[3]-V[1]**3))//B**~-m%B//3);m+=1
