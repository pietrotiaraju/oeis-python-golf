f=lambda n,k,m:k and sum(f(n-j**3,k-1,j)for j in range(m+1)if j**3<=n)or n<1
n=0
while[f(n,4,n)>1==print(n)]:n+=1
