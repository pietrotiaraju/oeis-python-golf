m=4
while[print(-~m*sum(((2**m+1)**m>>m*k)%2**m*(k**(m-k)-k)for k in range(m)))]:m+=1
