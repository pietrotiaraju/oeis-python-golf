m=1
while 1:
 T={(1,*[0]*m):1}
 for k in[*[1]*~-m,0]*m:
  for(a,b,*r),v in(T,T:={})[0].items():
   for R in{0,k}&{z:=0**a+0**b|a&b,z-1}:D=z-R;M=(s:=a|b)//4*2|R|D<<m;T[u]=T.get(u:=(R*M,*[(x>>1,M)[x&s>0]for x in r],D*M),0)+v
 print(T[min(T)]);m+=2
