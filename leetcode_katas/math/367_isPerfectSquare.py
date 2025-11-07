class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        l = 1
        r = int(num)

        while l <= r:
            mid = (r + l) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                r = mid - 1
            else:
                l = mid + 1

        return False

Solution().isPerfectSquare(14)