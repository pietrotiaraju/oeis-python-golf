h=lambda c,j:j<1or c>0<(h(c-(b:=c&-c),j)or h(c-b&~D*b,j-1))
n=2
while[print(max(m for m in range(n*-~n//2)for x in range(1<<m//2)if h(D:=x*2|int(f'{x:0{m}b}'[::-1],2),D.bit_count())>h(2**m-1,n)))]:n+=1
