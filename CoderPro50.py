def lengthOfLongestSubstring(str):
  letter_pos = {}
  start = -1
  end = 0
  max_length = 0

  while end < len(str):
    c = str[end]
    if c in letter_pos:
      start = max(start, letter_pos[c])    # Nice.  You don't have to remove values from the set.  Just move start. 

    max_length = max(max_length, end - start)

    letter_pos[c] = end
    end += 1
  return max_length


print(lengthOfLongestSubstring('aabcbbeacc'))
