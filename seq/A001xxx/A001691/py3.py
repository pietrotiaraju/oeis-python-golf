from itertools import*
def C(*g):
 G=F={*g}
 while F:F={tuple(x[i]for i in h)for x in F for h in g}-G;G|=F
 return G
n=1
while 1:P={*permutations(range(n))};d={};print(sum(d.get(k:=sum(n**len({g[i]for g in C(a)})for i in a))or d.setdefault(k,sum(C(a,b)==P for b in P))for a in P)//2);n+=1
