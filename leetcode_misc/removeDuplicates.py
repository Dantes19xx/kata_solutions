class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        n = len(nums)
        k = 1

        for i in range(1, n):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k

Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])