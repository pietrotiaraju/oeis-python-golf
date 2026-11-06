n=1
while 1:print(n**1*sum(k*(5*k*k+1-6*n)for k in range(1,n+1)if n%k<1)//24);n+=1
