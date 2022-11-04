"""
Given a string s and a character c that occurs in s, return an array of
integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""
class Solution(object):
    def shortestToChar(self, str, char):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        lengths = [0] * len(str)
        prev = None
        for current, letter in enumerate(str):
            if letter == char:

                if prev is None:
                    start = 0
                else:
                    start = (current +prev) // 2 +1
                    #print((current + prev) // 2 + 1)

                lengths[start:current + 1] = range(current - start, -1, -1)
                #print(lengths, "here1")
                prev = current
            elif prev is not None:
                lengths[current] = current - prev
                #print(lengths, "here2")
        return lengths


test = Solution()
print(test.shortestToChar( "loveleetcode", "e"))


