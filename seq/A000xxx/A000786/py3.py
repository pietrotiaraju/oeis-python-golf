L=[1,3,2];n=0
while[print(sum(L[-3:])//6)]:
 n-=1
 for t in 0,1,2:L+=sum(d*[-d,d%2or-d//4,-~-d%3-1or(3-d)//9][t]*sum(L[3*d::3*d])for d in range(n,0))//n,
