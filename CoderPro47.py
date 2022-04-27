
class Solution(object):
  def calcAngle(self, h, m):
    hh = h * 360/12 + m * (360/12) / 60
    mm = m * 360/60
    return abs(hh - mm)

print(Solution().calcAngle(3, 15))
# 7.50
print(Solution().calcAngle(3, 00))
# 90