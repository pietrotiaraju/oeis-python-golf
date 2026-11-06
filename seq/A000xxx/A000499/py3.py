n=1
while 1:print(n**3*sum(k*(2*k*k+1-3*n)for k in range(1,n+1)if n%k<1)//24);n+=1
