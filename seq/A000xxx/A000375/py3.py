from itertools import*
f=lambda d:(k:=d[0])and-~f(d[k::-1]+d[k+1:])
n=1
while[print(max(map(f,permutations(range(n)))))]:n+=1
