from itertools import*
n=0;C=combinations
while 1:R=range(n);print(len({min(sum(1<<sum(1<<p[i]for i in t)for t in T)for p in permutations(R))for k in range(1<<n)for T in C(C(R,3),k)if all({*C(sorted(S),3)}<={*T}for t,u in C(T,2)if len(S:={*t,*u})<5)}));n+=1
