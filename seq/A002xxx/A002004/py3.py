f=lambda s:max([len(s)]+[f(s+[a])for a in{*range(n)[:len({*s})+1]}-{*s[-1:]}if all(any(c not in x for c in(a,b)*2)for b in{*s}-{a}if(x:=iter(s)))])
n=1
while[print(f([]))]:n+=1
