n=k=0;s=[];d={}
while 1:
 if n==k*k:
  s+=[n];k+=1
  for x in s:d[n+x]=d.get(n+x,0)+1
 if d.get(n,0)==3:print(n)
 n+=1
