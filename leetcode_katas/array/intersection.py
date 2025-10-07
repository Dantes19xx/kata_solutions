class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        intersected = set()

        for i in nums1:
            if i in nums2:
                intersected.add(i)

        return list(intersected)

Solution().intersection([4,9,5], [9,4,9,8,4])