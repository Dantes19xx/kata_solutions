class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_arr = s.strip().split()
        res = " ".join(s_arr[::-1])

        return res

Solution().reverseWords("the sky    is blue")