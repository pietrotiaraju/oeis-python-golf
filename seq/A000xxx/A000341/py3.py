f=lambda s:s<{0}or sum(f(s-{i})for i in s if{i+len(s)}-C)
n=1
while R:=range(3,4*n,2):C={a*b//2for a in R for b in R};print(f({*range(n)}));n+=1
