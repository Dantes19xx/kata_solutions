class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)

        for i in range(l):
            is_uniq = True
            uniq_char = s[i]
            counter = 0

            while counter < l and is_uniq:
                if i != counter and s[counter] == uniq_char:
                    is_uniq = False

                counter += 1

            if is_uniq:
                return i
        
        return -1


Solution().firstUniqChar("aabb")