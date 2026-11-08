M=3
while 1:
 P=1;R={*range(M//2+1,M)}
 for w in R:S=R&{w*2**i%M for i in R};P*=w<max(S)or~-2**len(S)
 print(P);M-=~M
