m=1
while X:=4**m:V=P=[1]*4*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];_,a,b,c,d,*_=V;print((a*~-a+X*(b*(a*a+b)//2+a*c+d))//X**~-m%X//4);m+=1