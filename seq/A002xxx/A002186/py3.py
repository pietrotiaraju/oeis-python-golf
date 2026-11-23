g=[]
while 1:print(x:=min({*range(9)}-{*map(int.__xor__,g+[99]+g,g[::-1]*2)}));g+=x,
