from itertools import*
def C(*g):
 G=F={*g}
 while F:F={tuple(x[i]for i in h)for x in F for h in g}-G;G|=F
 return G
n=1
while 1:P={*permutations(range(n))};print(sum(C(a,b)==P for a in P for b in P)//2);n+=1
