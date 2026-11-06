g=lambda d:max([-~g(d[k::-1]+d[k+1:])for k in d if d[k]==k>0]+[0])
d=[0]
while[print(g(d))]:d+=len(d),
