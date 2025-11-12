class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        neg_count = 0

        for i in grid:
            l = 0
            r = len(i) - 1

            while l <= r:
                mid = (r + l) // 2

                if i[mid] >= 0:
                    l = mid + 1
                elif i[mid] < 0:
                    neg_count += (r - mid) + 1
                    r = mid - 1

        return neg_count                  
    
Solution().countNegatives([[3,2],[1,0]])