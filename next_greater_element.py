"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
 determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = {}
        final = []
        stack = []

        for number in nums2:
            print(stack)
            print("here1")
            if len(stack) > 0 and stack[-1] <= number:
                while len(stack)>0 and stack[-1] <= number:
                    results[stack.pop()]  = number
                    print(results)
                    print("here2")

            stack.append(number)
        for number in nums1:
            print(final)
            print("here3")
            final.append(results.get(number, -1))
        return final


test = Solution()
print(test.nextGreaterElement([4,1,2], [1,3,4,2]))

