r=[s:=1,0]
while[print(s*r[-2])]:s=-s;r[-1:]=sum(d*sum(r[d::d])for d in range(-len(r),0)),0
