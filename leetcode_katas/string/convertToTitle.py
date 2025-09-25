from collections import deque


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        res_arr = []
        base = 26


        while columnNumber > 0:
            columnNumber -= 1
            res_arr.append(chr(columnNumber % base + 65))
            columnNumber //= base
        
        res_arr.reverse()

        return "".join(res_arr)




Solution().convertToTitle(701)