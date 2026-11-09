import re
s='0'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)
