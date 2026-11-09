from functools import*
r=[n:=0,1]
g=cache(lambda m,k:m<1or k and g(m,k-1)+sum(r[i]*g(m-k*i,k)for i in range(1,m//k+1)))
while[print(+g(-n,-n))]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
