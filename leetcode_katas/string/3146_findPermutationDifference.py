class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        h_table = {}
        res = 0

        for i in range(len(s)):
            h_table[s[i]] = i

        for i in range(len(t)):
            res += abs(h_table[t[i]] - i)

        return res
    

Solution().findPermutationDifference("abcde", "edbac")
