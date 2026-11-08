w='f{dvhorakyg|ewipsblzdxjqtcm'
g=lambda n:n>99and g(n//(k:=10**(2+(t:=n>999))))+'hu'[t]+g(n%k)or n>19and g(n%10)+'v'[:n%10]+w[n//10+17]+'i'or w[n-1:n]
d=1
while d<1e6:[*map(print,sorted(range(d&-2,d*10),key=lambda n:g(n)+'s'*(n%100==1)or'n'))];d*=10
