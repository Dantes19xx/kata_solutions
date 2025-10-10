from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2:list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


    
Solution().intersect([4,9,5, 9, 9], [9,4,9,8,4, 9]
)