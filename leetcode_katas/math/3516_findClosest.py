class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        
        first = abs(z - x)
        second = abs(z - y)

        if first < second:
            return 1
        
        elif first > second:
            return 2
        
        else:
            return 0
    
Solution().findClosest(2, 7, 4)