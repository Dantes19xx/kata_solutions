class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        
        res = 0

        for word in words:
            j = 0
            is_cons = True

            while j < len(word) and is_cons:
                if word[j] not in allowed:
                    is_cons = False
                j += 1

            if is_cons:
                res += 1

        return res

    
Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
