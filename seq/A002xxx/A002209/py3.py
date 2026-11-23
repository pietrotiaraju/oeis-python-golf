from fractions import*
v=[]
while v:=[x:=1-sum(map(Fraction,v,range(2,len(v)+2)))]+v:print(x.denominator)
