*q,r=1,0,0,[0,0]
for u in q:r=[u:=u+x for x in[0]+r];q+=u,;print(u)
