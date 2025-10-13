class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return(self.merge_sort(nums))        

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = len(arr) // 2
        left_side = self.merge_sort(arr[:pivot])
        right_side = self.merge_sort(arr[pivot:])

        return self.merge(left_side, right_side)

    def merge(self, left, right):
        i = 0
        j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1

            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])
        
        return res


print(Solution().sortArray([5,2,3,1]))
