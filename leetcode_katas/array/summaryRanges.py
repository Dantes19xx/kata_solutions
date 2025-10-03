class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        res = []
        i = 0

        while i < len(nums):
            curr_range = [str(nums[i])]
            j = i
            while j < len(nums) - 1 and nums[j + 1] - nums[j] == 1:
                curr_range.append(str(nums[j + 1]))
                j += 1
            
            i = int(j) + 1

            if len(curr_range) > 1:
                res.append(curr_range[0]+"->"+curr_range[-1])

            else:
                res.append(curr_range[0])

        return res

            
Solution().summaryRanges([0,2,3,4,6,8,9])