n=k=0;s=[];d={};a={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 a.setdefault(d.get(n,0),n)
 while t in a:print(a[t]);t+=1
 n+=1
