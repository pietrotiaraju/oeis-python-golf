P=1
while 1:
 m=P+1;d=2
 while d*d<=m:d+=m%d>0 or(m:=m//d)*0
 print(m);P*=m
