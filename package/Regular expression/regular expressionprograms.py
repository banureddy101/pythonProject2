import re

# char='hello how aree 554555*&^%$#@!you'
matches = re.findall(r"a.+a", "abcada")
print(matches)
