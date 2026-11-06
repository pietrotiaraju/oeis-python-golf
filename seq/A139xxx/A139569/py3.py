a,b=[3],[1,2]
while[*map(print,a)]:a,b=b,[2*(y&x%2-2)-x for x,y in zip(a+[0,0],[1]+b)]
