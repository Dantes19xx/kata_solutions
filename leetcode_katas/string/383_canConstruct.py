class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        ransomNote = [x for x in ransomNote]
        magazine = [x for x in magazine]

        for i in range(len(ransomNote)):
            is_faced = False
            j = 0
            while j < len(magazine) and not is_faced:
                if ransomNote[i] == magazine[j]:
                    ransomNote[i] = magazine[j] = "-"
                    is_faced = True

                j += 1
            
            if not is_faced:
                return False

        return True if len(set(ransomNote)) == 1 else False

    
Solution().canConstruct("aa", "ab")