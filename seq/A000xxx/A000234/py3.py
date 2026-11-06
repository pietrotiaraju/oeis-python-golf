f=lambda b,t,s:s**3>(v:=t*t*M-1)and f(b,t,(2*s+v//s//s)//3)or n<=b<=s or f(b+~s,t,s)+f(b,t+M,s+M)
n=M=1
while 1:
 try:print(f(n*M+n,M,M)-1);n+=1
 except:M*=2
