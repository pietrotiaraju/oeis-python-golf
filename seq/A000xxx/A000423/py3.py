a=[];s={2,3}
while s:
 n=min(s);s.remove(n);print(n);s|={n*x for x in a};a+=[n]
