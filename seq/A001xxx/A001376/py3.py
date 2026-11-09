f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or 4**(sum(sum(l*(j%l<1)for l in L)**3for j in range(M))//M)
n=M=1
while[print(f(n))]:n+=1;M*=n
