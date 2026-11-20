T=lambda u:min([k>>1^d+k&3for d in u]for k in range(8))
f=lambda t,h,B:t==T(t)and(sum(f(t+[d],q,B|{h+1,h-1,h+1j,h-1j})for d in range(4)if{q:=h+1j**d}-B)if len(t)<n else t==T(t[::-1]))
n=-1
while[print(+f([],0,{0}))]:n+=1
