class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        h_table = set(arr)
        count = 0

        for i in arr:
            if i + 1 in h_table:
                count += 1

        return count


Solution().countElements([1,2, 3])
