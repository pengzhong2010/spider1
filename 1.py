import re
a='{"ok":1,asdf}'
m=re.match(r'.*(\"ok\":1,).*',a)
if m:
    print 1
else:
    print 2

print m.groups()