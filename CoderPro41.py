# import heapq
# import collections
# md = collections.defaultdict(list)

from collections import defaultdict

def sortString(s):
    return "".join(sorted(s))

def groupAnagramWords(strs):
    # keys = list(map(sortString, strs))    # Note: sorted(string) returns a list of characters sorted
    # print(keys)
    md = defaultdict(list)
    for s in strs:
        md["".join(sortString(s))].append(s)   
    return list(md.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])
