f=lambda F,m=1:max(map(len,F))<k and max(m,*[f(F|{T-N|{m}for T in F},m+1)for N in F])
k=1
while[print(f({frozenset()}))]:k+=1
