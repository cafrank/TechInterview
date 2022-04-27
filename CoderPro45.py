

# Complexity:
#   Spece: Constant.  4 variables
#   Time:  O(n)   Sliding window scans the array

class Solution(object):
  def intersection(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [x for x in set1 if x in set2]    # Nice.

# Or use tehash tables

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)
