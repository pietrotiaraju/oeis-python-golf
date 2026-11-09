M=lambda s:s and({a:b,b:a,**m}for b in s if 1<b-(a:=min(s))<N-1for m in M(s-{a,b}))or[{}]
H=lambda c,F:c[N-1:]and{(*(sum(map(c.index,{-~v%N,~-v%N,m[v]}))for v in c),)}or{x for v in F-{*c}for x in H(c+[v],{-~v%N,~-v%N,m[v]})}
N=4;s={0}
while R:={*range(N)}:
 t=0
 for m in M(R):
  if H([*R],0)-s:t+=1;s|=H([],R)
 print(t);N+=2