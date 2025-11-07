class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(nums) - 1
        first = last = -1

        while l <= r:
            mid = (r + l) // 2

            if target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

            else:
                if first == -1 and last == -1:
                    first = last = int(mid)

                elif first > l and target == nums[first - 1]:
                    first -= 1
                
                elif r > last and target == nums[last + 1]:
                    last += 1
                
                else:
                    return [first, last]
                
        
        return [-1, -1]
                


    
Solution().searchRange([], 0)