p=[1];z=[s:=0]
while[print(p[len(z)-1])]:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)]
