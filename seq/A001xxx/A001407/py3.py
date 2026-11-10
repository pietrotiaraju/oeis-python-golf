import math
t=3
while 1:
 X=8**t**3;Y=X**(t-3);M=X*Y;P=1
 for a in 1,-5,10,-10,5,-1:
  for B in range(2*t*t):V=[(x,y,z)for x in range(B//t%t)for y in range(B%t)for z in range(t-B//t%t-B%t)if(x+y+z+B//t//t)%2];s=len(V);D=[1<<i|1<<j for i in range(s)for j in range(i)if math.dist(V[i],V[j])<2];E=len(D);w=[(1+X)**(E-d)*(1-X)**d for d in range(E+1)];P*=pow(sum(w[sum(0<g&e<e for e in D)]for g in range(1<<s))>>s,a,M)
  t-=1
 print((P+Y*-~X//2)%M//Y-X//2);t+=7
