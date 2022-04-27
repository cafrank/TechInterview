
class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __repr__(self):     # Like toString()
    result = self.val
    result += f"{self.left}" if self.left else ''
    result += f"{self.right}" if self.right else ''
    return result


class Solution(object):
  def invert(self, n):
    if n == None:
      return None
    n.left, n.right = self.invert(n.right), self.invert(n.left)
    return n

n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')

print(Solution().invert(n))
# acfbed
