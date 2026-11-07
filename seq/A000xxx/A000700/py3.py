p=[1];j=1
while[print(p[j//2])]:p=[*map(sum,zip(p+[0]*j,[0]*j+p))];j+=2
