from itertools import*
def g(L):
 F=sum(L,())
 if len(L)==n:S.add(min(sum(1<<sum(1<<(p,*q,*r).index(v)for v in l)for l in L)for p in R for q in permutations({*sum([l for l in L if p in l],())}-{p})for r in permutations({*R}-{p,*q})))
 for l in combinations(R,3):
  if l>L[-1]and sum(v<l[0]for v in F)==3*l[0]and max(len({*l}&{*m})for m in L)<2>max(map(F.count,l))-1:g(L+[l])
n=0
while n:=n+1:R=range(n);S=set();n>6and g([(0,1,2),(0,3,4),(0,5,6)]);print(len(S))
