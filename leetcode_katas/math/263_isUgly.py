class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False
        elif n == 1:
            return True
        
        while n > 1:
            if n % 5 == 0:
                n //= 5
            elif n % 3 == 0:
                n //= 3
            elif n % 2 == 0:
                n //= 2
            else:
                return False
            
        return True

    
Solution().isUgly(14)