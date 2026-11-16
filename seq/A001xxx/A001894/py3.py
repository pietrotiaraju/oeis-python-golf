p=[1,2,2,1];z=[s:=0]*3
while 1:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)];print(p[len(z)-4])
