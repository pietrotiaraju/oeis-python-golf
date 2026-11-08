g=lambda n:2**n-sum(g(d)for d in range(1,n)if n%d<1)
s=n=1
while[print(s)]:n+=1;s+=g(n)//n
