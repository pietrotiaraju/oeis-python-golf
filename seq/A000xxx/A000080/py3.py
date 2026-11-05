from itertools import*
e=lambda T,s=1:2**n-1in[s:=s|t for t in T*n if s&t]
n=3;C=combinations
while 1:R=range(n);D={0};print(sum(e(T:=(7,)+U)>any(map(e,C(T,k)))==(T in D)!=D.update((*sorted(sum((t>>i&1)<<p[i]for i in R)for t in T),)for p in permutations(R))for k in R[:-2]for U in C([2*x for x in range(1<<n-1)if x.bit_count()==3],k)));n+=1
