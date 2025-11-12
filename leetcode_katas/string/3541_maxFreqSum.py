class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        h_table = {}

        for ch in s:
            if h_table.get(ch) is not None:
                h_table[ch] += 1
            else:
                h_table[ch] = 1
            
        max_vowel = 0
        max_consonant = 0

        for el in h_table:
            if el in "aeiou":
                if h_table[el] > max_vowel:
                    max_vowel = h_table[el]

            else:
                if h_table[el] > max_consonant:
                    max_consonant = h_table[el]

        return max_vowel + max_consonant

    
Solution().maxFreqSum("aeiaeia")