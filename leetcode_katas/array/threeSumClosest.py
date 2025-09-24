class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        arr = sorted(nums)
        closest_sum = arr[0] + arr[1] + arr[2]

        for i in range(len(arr) - 2):
            left = i + 1 
            right = len(arr) - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s

                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum



Solution().threeSumClosest([0, 1, 3, 5, 2, 6, 8], 7)