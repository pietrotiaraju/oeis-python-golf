n=0
while 1:Q=(n+2)**5;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*5);print(V*Q//Q**(5*n//2)%Q);n+=1
