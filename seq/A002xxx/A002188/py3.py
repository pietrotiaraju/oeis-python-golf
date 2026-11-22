g=[]
while 1:print(x:=min({*range(len(g)+1)}-{*map(int.__xor__,g[1:],g[:len(g)//2:-1])}));g+=x,
