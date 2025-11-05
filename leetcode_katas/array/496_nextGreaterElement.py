class Solution(object):
    def nextGreaterElement(self, nums1, nums2: list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []

        for i in nums1:
            ind_in_nums2 = nums2.index(i)
            j = ind_in_nums2 + 1
            next_greater = -1

            while j < len(nums2) and next_greater == -1:
                if nums2[j] > i:
                    next_greater = nums2[j]

                j += 1

            res.append(next_greater)

        return res


Solution().nextGreaterElement([5,4], [5,4,3,2,1])
