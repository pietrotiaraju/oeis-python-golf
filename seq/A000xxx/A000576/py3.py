from itertools import*
n=3
while[print(sum(all(len({*c})>n-3for c in zip(range(n),*R))for R in product(*[permutations({*range(n)}-{i})for i in range(n-3)])))]:n+=1
