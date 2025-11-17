class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        first = None

        for i in range(len(nums)):
            if nums[i] == 1:
                if first is None:
                    first = int(i)
                else:
                    if (i - first) - 1 < k:
                        return False
                    
                    first = int(i)

        return True    
        
            
        
    
Solution().kLengthApart([1,1,1,1], 0)