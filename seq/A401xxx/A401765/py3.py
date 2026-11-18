T="GGGRRRYBGGYBGgbbrrgyykkkkyrrggbbyyyykkkBGBGBGRGRYRGG"
h=lambda l,x,c,r="":[z for i in range(13)if c+l[0]in T[i::26]for z in h(l[1:],x or T[i],T[i+39],r+T[i+13])]if l else[r][x!=c:]
n=0
while 1:
 n+=1;S={('',)*n};m=-1
 while S:S={min(z[i:]+z[:i]for i in range(n))for l in S for z in h(l,'','')};m+=1
 print(m)

