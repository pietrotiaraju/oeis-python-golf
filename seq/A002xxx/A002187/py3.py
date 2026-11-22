g=[0]
while 1:print(x:=min({*range(10)}-{*map(int.__xor__,g,g[-2::-1])}));g+=x,
