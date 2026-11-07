s=[];t={n:=0}
while 1:
 if n==len(s)**2:s+=n,;t|={n+x for x in s}
 if{n-x for x in s}&t^{n}>{n}:print(n)
 n+=1