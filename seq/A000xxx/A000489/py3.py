n=r=q=p=0
while 1:
 n+=1;s=0;w=1
 for j in range(n+4):s+=w*j*(~-j*(j-2)*(r*w+6*q*p)//2+j*j*w*w);r,q,p,w=q,p,w,w*(n-j)//-~j
 print(s)
