from itertools import*
F=frozenset
n=2
while 1:
 P=[*permutations(range(n))];L={F(zip(p,p[::-1]))for p in P};H=lambda E,j=1:[E][:not E]+[t|{M}for M in L if(0,j)in M<=E for t in H(E-M,j+1)];S={*H(F().union(*L))};c=0
 while S:c+=1;x=S.pop();S-={F(F((p[a],p[b])for a,b in M)for M in x)for p in P}
 print(c);n+=2
