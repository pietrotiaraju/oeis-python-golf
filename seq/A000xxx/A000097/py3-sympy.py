from sympy import*
s=n=u=v=0
while 1:s+=partition(n);u,v=v,u+s;print(v);n+=1
