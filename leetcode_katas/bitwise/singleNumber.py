class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0

        for i in nums:
            res = res ^ i

        return res


Solution().singleNumber([4,1,2,1,2])