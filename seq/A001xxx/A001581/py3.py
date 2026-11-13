P={m:=0}
while 1:
 m+=1;a=b=1
 while(m-b in P)<(b<=m):a,b=b,a+b
 if b>m:P|={m};print(m)
