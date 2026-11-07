m=2
while[print(-~m*sum(((2**m+1)**m>>m*k)%2**m*k**(m-k)for k in range(m)))]:m+=1
