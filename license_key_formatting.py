"""
You are given a license key represented as a string s
that consists of only alphanumeric characters and dashes.
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains
exactly k characters, except for the first group, which could
be shorter than k but still must contain at least one character.
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
"""

class Solution(object):
    def licenseKeyFormatting(self, str, group_size):
        """
        :type str: str
        :type group_size: int
        :rtype: str
        """
        str = str.replace('-','')
        str =str.upper()
        str = str[::-1]
        final_string = ''
        count = 0
        for license_letter in str:
            if count == group_size:
                final_string+= '-'
                count = 0
            final_string += license_letter
            count +=1
        return final_string[::-1]
test = Solution()
print(test.licenseKeyFormatting("2-5g-3-J", 2))