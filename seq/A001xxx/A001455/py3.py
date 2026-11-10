D={15:1}
while[s:=0]:
 for l in[*D]:
  f=D.pop(l);s+=~l%2*f*f;c=l&~l>>1
  while c:b=c&-c;D[l+b]=D.get(l+b,0)+f;c-=b
 s and print(s)
