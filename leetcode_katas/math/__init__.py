class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def recur(digit):
            if digit == 1:
                return True
            elif digit < 1 or digit % 3 != 0:
                return False
            
            return recur(digit // 3)
        
        if n == 1:
            return True

        return recur(n)

    
Solution().isPowerOfThree(19684)