#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number = {}
        complement = {}
        for num in nums:
            number[num] = number.get(num, 0) + 1
        for index, num in enumerate(nums):
            if num != target - num:
                if number.get(target-num, 0) >= 1:
                    return [index, self.find(nums, target-num, index)]
            else:
                if number.get(target-num, 0) > 1:
                    return [index, self.find(nums, target-num, index)]

    def find(self, nums, value, index):
        for idx in range(index+1, len(nums)):
            if nums[idx] == value:
                return idx

# @lc code=end
