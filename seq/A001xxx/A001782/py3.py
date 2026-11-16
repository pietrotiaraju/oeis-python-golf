p=q=[1]
while 1:
 p,q=p+q,p+[-x for x in q];A=p;B=[i*x for i,x in enumerate(p)][1:];g=h=1;s=p[-2]
 while B[1:]:a=len(A);d=a-len(B);s*=(a|d)%2or-1;exec("A=[B[0]*x-A[0]*y for x,y in zip(A,B+[0]*d)][1:];"*-~d+"\nwhile[0]==A[:1]<A:A=A[1:]");A,B=B,[x//g//h**d for x in A];g=A[0];h=g**d//h**~-d
 print(s*B[0]**~-len(A)//h**(len(A)-2))
