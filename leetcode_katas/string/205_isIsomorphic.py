class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        h1 = {}
        h2 = {}

        for i in range(len(s)):
            if h1.get(s[i]):
                if h1[s[i]] != t[i]:
                    return False
            
            if h2.get(t[i]):
                if h2[t[i]] != s[i]:
                    return False
            h1[s[i]] = t[i]
            h2[t[i]] = s[i]

        return True
    
Solution().isIsomorphic("egg", "add")