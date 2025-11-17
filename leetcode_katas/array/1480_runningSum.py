class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        local_sum = 0

        for i in nums:
            local_sum += i
            output.append(local_sum)

        return output

    
Solution().runningSum([1,2,3,4])