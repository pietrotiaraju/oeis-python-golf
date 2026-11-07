P=[1,*[0]*65]*32
f=n=1
while[print(min(f,sum(P[::66])))]:f*=n;n+=1;P=[sum(P[x+x%64-d]for d in(2,4,8,16,32,64)if d&2*x>x&32)for x in range(1,2049)]
