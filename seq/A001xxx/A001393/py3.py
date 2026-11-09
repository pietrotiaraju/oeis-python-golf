t=3
while 1:
 X=8**t**3;Y=X**(2*t-6);M=X*Y;P=1
 for a in 1,-5,10,-10,5,-1:
  for B in range(t**3):L=B//t;B%=t;s=L*B*max(t-L-B,0);D=[1+2**k<<i for k,q in((1,L),(L,L*B),(L*B,s))for i in range(s)if i%q<q-k];E=len(D);w=[(1+X)**(E-d)*(1-X)**d for d in range(E+1)];P*=pow(sum(w[sum(0<g&e<e for e in D)]for g in range(1<<s))>>s,a,M)
  t-=1
 print((P+Y*-~X//2)%M//Y-X//2);t+=7
