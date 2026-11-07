L=[1,1]
while[print(L[-2])]:L+=sum(map(int.__mul__,L,L[-1:]+L[::-1])),;L[0]+=2
