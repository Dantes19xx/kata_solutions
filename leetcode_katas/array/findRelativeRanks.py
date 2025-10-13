class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        sorted_arr = sorted(score, reverse=True)
        #sorted_arr = self.counting_sort(score)

        first = sorted_arr[0] if len(sorted_arr) >= 1 else None
        second = sorted_arr[1] if len(sorted_arr) >= 2 else None
        third = sorted_arr[2] if len(sorted_arr) >= 3 else None
        score_place = [0] * len(score)

        for i in range(len(sorted_arr)):
            if sorted_arr[i] == first:
                score_place[score.index(sorted_arr[i])] = "Gold Medal"
            elif sorted_arr[i] == second:
                score_place[score.index(sorted_arr[i])] = "Silver Medal"
            elif sorted_arr[i] == third:
                score_place[score.index(sorted_arr[i])] = "Bronze Medal"
            else:
                score_place[score.index(sorted_arr[i])] = str(i + 1)

        return score_place

    def counting_sort(self, arr):
        
        maximum = max(arr)
        minimum = min(arr)

        count = [0] * (maximum - minimum + 1)

        for i in arr:
            count[i - minimum] += 1

        res = []

        for ind, val in enumerate(count):
            res.extend([ind + minimum] * val)

        return res
            
        
Solution().findRelativeRanks([4, 10])