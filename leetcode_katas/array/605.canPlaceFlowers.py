class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if len(flowerbed) == 1:
            if set(flowerbed[0:2]) == {0}:
                return True if n >= 0 else False
            else:
                return True if n == 0 else False

        if flowerbed[0] == 0 and flowerbed[1] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n > 0:
            flowerbed[-1] = 1
            n -= 1

        i = 1

        while n > 0 and i < len(flowerbed) - 1:
            if set(flowerbed[i-1:i+2]) == {0}:
                flowerbed[i] = 1
                n -= 1
            
            i += 1
            
        return not bool(n)


        
Solution().canPlaceFlowers([0], 0)