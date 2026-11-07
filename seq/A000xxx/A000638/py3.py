from itertools import*
n=0;D=[]
while S:=[*permutations(range(n))]:
 for K in(L:=[{S[0]}]):
  for g in S:
   J=K|{g}
   while J<(J:={tuple(a[i]for i in b)for a in J for b in J}):0
   if J not in D:D+=[{tuple(s.index(p[x])for x in s)for p in J}for s in S];L+=J,
 print(len(L)-1);n+=1
