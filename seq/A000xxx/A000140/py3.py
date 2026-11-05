p=[1];z=[s:=0]
while[print(max(p))]:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)]