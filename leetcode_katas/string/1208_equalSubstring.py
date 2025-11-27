class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
        current_cost = 0
        current_len = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            current_len = right - left + 1

            if current_len > max_len:
                max_len = int(current_len)

        return max_len


Solution().equalSubstring(s = "thjdoffka", t = "qhrnlntls", maxCost = 11)
