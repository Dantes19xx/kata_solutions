class Solution(object):
    def thirdMax(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # nums = self.insert_sort(list(set(nums)))

        nums = sorted(list(set(nums)), reverse=True)

        if len(nums) >= 3:
            return nums[2]
        
        return nums[0]


        
    def insert_sort(self, arr):
        for i in range(len(arr)-1, -1, -1):
            j = i
            while j < len(arr) - 1 and arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                j += 1

        return arr
    

    
Solution().thirdMax([2,2,3,1])