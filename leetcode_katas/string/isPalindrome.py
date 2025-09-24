import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        formatted = re.findall(r"[a-z0-9]", s.lower())

        return True if formatted == formatted[::-1] else False

        a = 1
        
    
Solution().isPalindrome("0P")