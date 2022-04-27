import heapq
import collections
from collections import defaultdict

md = collections.defaultdict(list)      # multimap
md = defaultdict(list)
md['abc'].append('abc')   
md['abc'].append('bca')   
md['efg'].append('gef')   
md['efg'].append('efg')   

my_list = [4, 9, 5]
my_set = set(my_list)
