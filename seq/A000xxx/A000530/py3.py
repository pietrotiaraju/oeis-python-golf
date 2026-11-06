from functools import*
n=0
while 1:
 n+=1
 @cache
 def f(a,b,r,s,t,u):
  if a+r>=2*n:return 1
  if b+s>=2*n:return 0
  v=t+1 if u==0 else 1;w=t+1 if u==1 else 1
  return f(a+1,b,max(r,v),s,v,0)+f(a,b+1,r,max(s,w),w,1)
 print(f(0,0,0,0,0,0))
