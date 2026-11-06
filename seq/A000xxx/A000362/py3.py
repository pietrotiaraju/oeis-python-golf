D=[b:=0]
while 1:b+=2;D+=0,sum((v:=y*y%(2*b)-b)**3*(2*b-abs(v))-b**3*v-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(D[b]>>(b>2))
