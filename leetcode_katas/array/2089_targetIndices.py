class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        res = []
        first = -1
        last = -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                if first == -1 and last == -1:
                    first = last = mid
                
                elif first > l and nums[first - 1] == target:
                    first -= 1
                
                elif last < r and nums[last + 1] == target:
                    last += 1
                
                else:
                    if first == last:
                        return [first]
                    
                    res = [x for x in range(first, last + 1)]

                    return res

        return []



    
Solution().targetIndices([100,1,100], 100)
