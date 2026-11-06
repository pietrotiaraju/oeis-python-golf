g=1;v=0
def f(E):L=sum(E,(0,));U={x for x in range(v)if L.count(x)<6};B={i:=min(U|{v})};exec('B|={b for a,b in E if a in B};'*g);return i==v or any(f(E+[(i,j),(j,i)])for j in U-B if~-j in L)
while 1:v+=2;g+=f([])!=0!=print(v)
