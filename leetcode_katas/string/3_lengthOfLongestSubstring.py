class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        l = set()
        max_len = 0

        for i in range(len(s)):
            repeated_char = False
            l.add(s[i])
            j = i + 1
            while not repeated_char and j < len(s):
                if s[j] not in l:
                    l.add(s[j])
                else:
                    repeated_char = True
                
                j += 1
                
            if max_len < len(l):
                max_len = len(l)
            l = set()

        if not max_len:
            max_len = len(l)

        return max_len
        
    
Solution().lengthOfLongestSubstring("jbpnbwwd")
