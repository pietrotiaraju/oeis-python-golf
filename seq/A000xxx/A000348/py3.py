f=lambda s:s<{0}or sum(f(s-{o})for o in s if{o*o+4*len(s)**2}-C)
n=1
while R:=range(3,4*n*n,2):C={a*b for a in R for b in R};print(f({*range(1,2*n,2)}));n+=1
