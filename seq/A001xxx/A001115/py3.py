P=[1];n=0
while[print(P[n]+sum(P[1:n//2+1]))]:n+=1;P+=(2**n-sum(d*P[d]for d in range(1,n)if n%d<1))//n,
