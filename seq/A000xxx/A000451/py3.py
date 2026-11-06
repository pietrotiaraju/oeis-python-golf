n=k=0;s=[];d={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 while t<=d.get(n,0):print(n);t+=1
 n+=1
