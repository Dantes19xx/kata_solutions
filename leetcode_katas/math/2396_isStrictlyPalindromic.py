class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for base in range(2, n - 1):
            curr_digit = int(n)
            res = []

            while curr_digit > 0:
                res.append(str(curr_digit % base))
                curr_digit //= base

            if res != res[::-1]:
                return False
        
        return True
    
Solution().isStrictlyPalindromic(3)