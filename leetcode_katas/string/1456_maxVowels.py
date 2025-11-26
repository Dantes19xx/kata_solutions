class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        s_arr = [x for x in s]
        left = right = 0
        max_vow = float('-inf')
        curr_vow = 0
        window = 0

        while left < len(s_arr) - k + 1:
            if s_arr[right] in "aeiou":
                curr_vow += 1
            
            window += 1
            if window == k:
                if curr_vow > max_vow:
                    max_vow = int(curr_vow)

                if s_arr[left] in "aeiou":
                    curr_vow -= 1
                
                left += 1
                window -= 1
            
            right += 1

        return max_vow

        
    
Solution().maxVowels("leetcode", 3)