class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l = 1
        r = int(x)

        while l <= r:
            mid = (r + l) // 2
            sq = mid * mid

            if sq < x:
                l = mid + 1

            elif sq > x:
               
                r = mid - 1
                

            else:
                return mid
            
        return r
            
    
Solution().mySqrt(7)
