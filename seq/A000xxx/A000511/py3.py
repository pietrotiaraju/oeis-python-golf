f=lambda z,d,t,S:n<len(S)or sum(f(w,a,b,S|{w})for a,b in((d,t),(t,-d-t))if{w:=z+a}-S)
n=0
while[print(+f(1,1,1j,{0,1}))]:n+=1
