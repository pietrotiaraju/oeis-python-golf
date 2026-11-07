f=lambda m,n:m<2or sum(f(m-1,k:=i.bit_count())<<k*(n-k)for i in range(2**n))
n=1
while[print(f(3,n)//3)]:n+=1
