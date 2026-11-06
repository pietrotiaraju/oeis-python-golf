f=lambda x:sum(map(int.__mul__,L,x))
r=[1,1];L=[1];n=0
while[print(n and r[1])]:n-=1;L+=f(r),;r=[sum(d*(L[-d]+f(r[d-1::2]))*sum(r[~d:-1:-d])for d in range(n,0))//2//n]+r
