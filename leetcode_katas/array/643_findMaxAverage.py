class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left = 0
        curr_sum = 0
        max_av = float('-inf')

        for right in range(len(nums)):
            if (right - left) + 1 == k:
                curr_sum += nums[right]
                av = curr_sum / k
                if av > max_av:
                    max_av = av
                
                curr_sum -= nums[left]
                left += 1
            else:
                curr_sum += nums[right]
            
        return max_av

    
Solution().findMaxAverage([1,12,-5,-6,50,3], 4)