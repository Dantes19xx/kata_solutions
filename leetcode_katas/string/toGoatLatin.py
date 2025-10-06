class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        
        vowels = "aeiou"
        arr_sent = sentence.split(" ")
        res = ""

        for i in range(len(arr_sent)):
            a_mult = "a" * (i + 1)
            if arr_sent[i][0].lower() in vowels:
                res += arr_sent[i]+"ma"+a_mult+" "

            else:
                res += arr_sent[i][1:]+arr_sent[i][0]+"ma"+a_mult+" "
                

        return res.rstrip()

Solution().toGoatLatin("I speak Goat Latin")