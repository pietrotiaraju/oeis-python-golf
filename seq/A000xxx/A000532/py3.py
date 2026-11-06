from functools import*
n=0
while 1:
 n+=1
 @cache
 def f(v,S):
  if v==n*(n-1):return int(S==(1<<(n*n))-1)
  return sum(f(w,S|1<<w)for w in(v-n,v+n,v-1,v+1)if 0<=w<n*n and abs(w//n-v//n)+abs(w%n-v%n)==1 and S>>w&1==0)
 print(f(0,1))
