"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices
(inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
"""
class Solution(object):
    def largeGroupPositions(self, str):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        groups = []
        count = 1
        str += " "

        for current, letter in enumerate(str[1:], 1):
            if letter == str[current-count]:
                #print(start)
                #print(current, count)
                #print(str[current-count])
                count += 1
            else:
                if count >= 3:
                    groups.append([current-count, current-1])
                count = 1

        return groups

test = Solution()
print(test.largeGroupPositions("abcdddeeeeaabbbcd"))