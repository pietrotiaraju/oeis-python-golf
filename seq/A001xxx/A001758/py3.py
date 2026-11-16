r=[0,2,2]
while 1:s=0;r=[s:=s+x for x in[0]+r[::-1]];print(s-2*r[1])
