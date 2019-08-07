from itertools import dropwhile

with open('somefile.txt') as f:
    for line in dropwhile(lambda  line: line.startswith('#'), f):
        print(line, end = '')

from itertools import  islice
items = ['a', 'b', 'c', 1, 2, 3, 4]

for x in islice(items, 3, None):
    print(x)

with open("somefile.txt") as f:
    for i in f:
        if i.startswith("#"):
            pass
        else:
            print(i)