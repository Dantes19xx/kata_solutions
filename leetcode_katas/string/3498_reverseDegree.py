class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0

        for i in range(len(s)):
            res += abs((ord(s[i]) - ord("a") - 26)) * (i + 1)
        
        return res
    
Solution().reverseDegree("zaza")