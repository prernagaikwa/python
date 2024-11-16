import re
str="hello world@#, i am here"
match=re.escape(str)
print(match)