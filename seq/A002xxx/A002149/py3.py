B=2383747;C=[0]*B;n=0
for a in range(3,999,2):
 for b in range(1,a,2):C[s::t]=map((1).__add__,C[(s:=4*a*a+8*a-b*b)::(t:=8*a)])
while 1:print(next(p for p in range(B-8|n//50<<180*n,0,-8)if(p<B and C[p]or(4*sum(pow(k,p//2,p)<2for k in range(p//2+1))-p-9)//12)==n and all(p%d for d in range(2,p))));n+=1
