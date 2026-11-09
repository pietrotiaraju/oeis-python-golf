import re
s='10'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:f'{len(m[0]):b}'+m[1],s)
