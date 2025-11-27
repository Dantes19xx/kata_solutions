class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pr = [nums[0]]

        for i in range(1, len(nums)):
            pr.append(nums[i] + pr[-1])

        if pr[-1] - pr[0] == 0:
            return 0
        
        for i in range(1, len(pr)-1):
            if pr[i-1] == pr[len(pr)-1] - pr[i]:
                return i
            
        if pr[-2] == 0:
            return len(pr) - 1
        
        return -1
            
        
    
Solution().findMiddleIndex([3,2,-1,-4,8])