

# Complexity:
#   Spece: Constant.  4 variables
#   Time:  O(n)   Sliding window scans the array

class Solution(object):
  def findRanges(self, nums):
    leftIndex = currIndex = rightIndex = sum = 0
    minLen = float('inf')

    while rightIndex < len(nums):
        while nums[rightIndex] - nums[currIndex] < 2:
            rightIndex += 1

        if leftIndex == rightIndex:
            print(leftIndex)
        else:
            print(leftIndex, "->", rightIndex)
        leftIndex = rightIndex
        rightIndex += 1

print(Solution().findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0-2', '5-5', '7-11', '15-15']