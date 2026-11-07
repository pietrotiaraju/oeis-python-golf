n=1
while[print(sum(1<<(k:=i.bit_count())*(n-k)for i in range(2**~-n)))]:n+=1
