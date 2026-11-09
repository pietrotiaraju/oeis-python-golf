l=[n:=1,0]
while[print(l[n])]:
 n+=1;d=2
 while n%d:d+=1
 l+=l[n//d]+d,
