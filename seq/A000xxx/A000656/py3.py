n=1
while 1:
 D={};a=c=0
 for i in range((N:=2**n)**n*2):
  for _ in[m:=[s:=0]]*n:m+=[y^i%N for y in m];s+=i%N;i>>=n
  z=len({*m})>>n;l=[]
  for x in m*z:
   j=-1
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+(i<1>s>>n<z);a+=i*d*z;c+=i*z>0
 print(a//c//sum(D.values()));n+=1
