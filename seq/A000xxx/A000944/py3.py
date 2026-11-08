from itertools import*
Q=lambda C,k:any({1<<a|1<<b for a in p[:3]for b in p[-3:]}<=C for p in P)or k>0and any(Q({d^c*(d&c>c&-c)for d in C}-{0},k-1)for c in C)
n=1
while 1:R=range(n);P=[*permutations(R)];E=[1<<a|1<<b for b in R for a in range(b)];print(len({min(sum(1<<sum((d>>i&1)<<p[i]for i in R)for d in G)for p in P)for m in range(3*n+1>>1,3*n-5)for G in combinations(E,m)if all([s:=~r&r+1]+[s:=s|d for d in G*n if d&r<1<=d&s]and s+r+1>>n for r in E)>Q({*G},n-6)}));n+=1
