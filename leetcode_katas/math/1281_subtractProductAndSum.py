class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = [int(x) for x in str(n)]

        s = sum(nums)
        mult = 1

        for i in nums:
            mult *= i

        return mult - s
    
Solution().subtractProductAndSum(234)
