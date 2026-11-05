from itertools import*
c=lambda K:K<(T:={tuple(a[i]for i in b)for a in K for b in K})and c(T)or K
n=1
while 1:
 P=[*permutations(R:=range(n))];L=[{P[0]}]
 for H in L:
  D={*H}
  for g in P:
   if{g}-D:K=c(H|{g});D|={tuple(a[i]for i in g)for a in H};L+=[K][K in L:]
 print(sum({tuple(s[k[s.index(i)]]for i in R)for k in K}==K for K in L if n<=len(K)*all(any(len({*B,*(k[x]for x in B)})%m for k in K)for m in range(2,n)for B in combinations(R,m))for s in P)//len(P));n+=1
