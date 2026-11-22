from fractions import*
w=[]
while w:=[y:=Fraction(j:=1,len(w)+1)]+[y:=(y/j-j*x)/(4*(j:=j+1)-2)for x in w]:print(y.denominator)
