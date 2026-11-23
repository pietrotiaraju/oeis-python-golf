from fractions import*
v=[]
while v:=[x:=-sum(map(Fraction,v,range(2,len(v)+2)))or 1]+v:print(x.denominator)
