C=[]
while 1:C+=-sum((-1)**k*sum(C[k*(1-3*k)::-2*k][:2],k*k+k==len(C))for k in range(1,len(C))),0;print(C[-2]or 1)
