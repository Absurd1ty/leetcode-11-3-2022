"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for number in nums:
            if number == 1:
                count +=1
            else:
                max_count = max(count, max_count)
                count = 0

        return max(count, max_count)