*q,r=0,1,0,[]
for u in q:print(u);r=[u:=u+x for x in[0]+r];q+=u,
