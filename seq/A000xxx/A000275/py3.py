b=n=1;c=[1]
for x in c:print(abs(x));c+=-sum(c[~k]*(b:=b*(k-n)//~k)**2for k in range(n)),;n+=1
