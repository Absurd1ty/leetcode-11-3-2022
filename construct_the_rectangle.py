"""
A web developer needs to know how to design a web page's size.
So, given a specific rectangular web page’s area, your job by now is to
design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        """
        really slow 
        """
        """
        length = int(area**0.5)
        width = int(area**0.5)

        while length * width != area:
            if length * width < area:
                length += 1
            else:
                width -= 1
        return [length, width]
        """
        middle = int(area**0.5)
        while area % middle != 0:
            middle -= 1
        return [int(area/middle), middle]
test = Solution()
print(test.constructRectangle(24))