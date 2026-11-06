n=1
while 1:print(n**2*sum(k*(3*k*k+1-4*n)for k in range(1,n+1)if n%k<1)//24);n+=1
