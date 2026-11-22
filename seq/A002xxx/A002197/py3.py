from fractions import*
w=[]
while w:=[y:=Fraction(j:=1,16*len(w)+24)]+[y:=(j*j*x-y/4)/(j-~j)/(j:=j+1)/2for x in w]:print(y.numerator)
