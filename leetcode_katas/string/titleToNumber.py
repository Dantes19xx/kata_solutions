class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        res = 0
        l = len(columnTitle)
        base = 26
        pow_idx = 0

        for i in range(l-1, -1, -1):
            res += (ord(columnTitle[i]) - 64) * pow(base, pow_idx)
            pow_idx += 1

        return res



Solution().titleToNumber("ZZ")