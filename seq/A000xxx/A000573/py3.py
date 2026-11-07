from itertools import*
n=4
while[print(sum(all(len({*c})>3for c in zip(range(n),*R))for R in product(*[permutations({*range(n)}-{i})for i in(0,1,2)])))]:n+=1
