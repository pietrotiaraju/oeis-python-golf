D=[b:=0]
while 1:b+=2;D+=0,sum((v:=y*y%(2*b)-b)*(abs(v)-b)-D[b//y*(y%2>b%y)]for y in range(2,b+2));print(-~D[b]>>1)