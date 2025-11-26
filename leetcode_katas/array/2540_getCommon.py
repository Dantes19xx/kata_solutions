class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        res = set(nums1)
        minimum = float('inf')

        for d in nums2:
            if d in res:
                if minimum > d:
                    minimum = d

        return minimum if minimum != float('inf') else -1
    
Solution().getCommon([1,2,3], [2, 4, 1])