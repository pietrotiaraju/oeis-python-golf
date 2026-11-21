B=2383747;C=[0]*B;n=0
for a in range(2,999):
 for b in range(1,a,2):C[s::t]=map((1).__add__,C[(s:=4*a*-~a-b*b)::(t:=4*a<<a%2)])
while 1:print(next(p for p in range(B-4|n//50<<180*n,0,-8)if(p<B and C[p]or p//4-sum(pow(k,p//2,p)>1for k in range(p//2+1)))==n and all(p%d for d in range(2,p))));n+=1
