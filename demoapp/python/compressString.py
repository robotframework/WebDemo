# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = groupby(input())
for k, g in s:
    print((len(list(g)),int(k)),end=' ')
   # print((len(list(g)), int(k)),end = ' ')
