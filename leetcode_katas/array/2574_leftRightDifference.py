class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_sum = [0]
        right_sum = [0]

        for i in range(1, len(nums)):
            left_sum.append(nums[i-1] + left_sum[-1])

        for j in range(len(nums)-2, -1, -1):
            right_sum.append(nums[j+1] + right_sum[-1])

        right_sum.reverse()

        res = []
        for k in range(len(nums)):
            res.append(abs(left_sum[k] - right_sum[k]))

        return res
        
    
Solution().leftRightDifference([10,4,8,3])