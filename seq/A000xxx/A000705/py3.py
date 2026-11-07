from decimal import*
c=getcontext();m=1
while 1:
 K=sorted((c.ln(p)/(c.ln(j+1)-c.ln(j)),p)for p in range(2<<m)for j in range(1,3*m)if p*j**-~m//(j+1)**m==j>0<all(p%d for d in range(2,p)));t=min(b[0]-a[0]for a,b in zip(K,K[1:]))*10**c.prec>m**3<<9;m+=t;c.prec*=2-t
 for _,p in K*t:print(p)
