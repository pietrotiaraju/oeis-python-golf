P=[1,*[0]*33]*16
f=n=1
while[print(min(f,sum(P[::34])))]:f*=n;n+=1;P=[sum(P[x+x%32-d]for d in(2,4,8,16,32)if d&2*x>x&16)for x in range(1,513)]
