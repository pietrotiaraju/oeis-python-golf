*l,c=1,0
while[*map(print,l[c:])]:c=-len(l)-c;l+=map(sum,zip(l,l[~c::-1]))
