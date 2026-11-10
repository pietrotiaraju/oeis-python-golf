C=[]
f=lambda:-sum((-1)**k*sum(C[k*(1-3*k)::-2*k][:2],k*k+k==len(C))for k in range(1,len(C)))
while 1:C+=f(),;C+=C[-1]+f(),;print(C[-1]or 1)
