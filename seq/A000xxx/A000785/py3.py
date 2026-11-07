g=lambda B,s,x=[]:(x and g(x+[-1],s)or s==0)+sum(g(B[1:],s+1-(3*v+2<<(x>[])),x+[v])for v in range(min(B[1]+1,s,*x[-1:])))
L=[1,-3,-1];n=0
while 1:n+=1;exec("L+=sum(d*[-d,d%2or-d//4,-~-d%3-1or(3-d)//9][len(L)%3]*sum(L[3*d::3*d])for d in range(-n,0))//-n,;"*3);print((sum(L[-3:])+3*g([n]*3*n,n))//6)
