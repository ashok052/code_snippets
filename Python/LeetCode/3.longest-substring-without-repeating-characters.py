#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        start = 0
        while True:
            curr_len = 0
            if start == len(s):
                break
            for char in s[start:]:
                if char not in char_set:
                    curr_len += 1
                    char_set.add(char)
                    if curr_len > max_len:
                        max_len = curr_len
                else:
                    char_set.clear()
                    start += 1
                    if curr_len > max_len:
                        max_len = curr_len
                    break
        return max_len

# @lc code=end
