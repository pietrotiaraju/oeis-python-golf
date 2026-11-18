n=0
while 1:Q=(n+2)**6;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*6);print(V*Q//Q**(3*n)%Q);n+=1
