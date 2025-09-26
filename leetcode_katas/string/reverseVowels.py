class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        s = [x for x in s]
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].lower() in vowels:
                while s[j].lower() not in vowels:
                    j -= 1

                s[i], s[j] = s[j], s[i]
                j -= 1

            i += 1

        return "".join(s)



Solution().reverseVowels("leetcode")