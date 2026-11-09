import re
s='1'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str((k:=len(m[0]))+k//3*7)+m[1],s)
