import re
p=re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

q=re.compile('\d')
print(q.findall("11 A.M on 4th july 1886"))

r=re.compile('\d+')
print(r.findall("11 A.M on 4th july 1886"))

s=re.compile('ab*')
print(s.findall('abbbaabbb'))
