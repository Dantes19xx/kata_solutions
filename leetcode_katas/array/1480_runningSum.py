class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = [nums[0]]

        for i in range(1, len(nums)):
            output.append(nums[i] + output[-1])

        return output

    
Solution().runningSum([1,2,3,4])