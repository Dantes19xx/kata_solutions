class Solution(object):
    def __init__(self):
        self.roman_signs_solo = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        self.roman_signs_double = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        curr = 0
        count = 0

        while count != len(s):
            curr = self.roman_signs_double.get(s[count:count+2])
            if curr is None:
                res += self.roman_signs_solo.get(s[count], 0)
                count += 1

            else:
                res += curr
                count += 2

        return res
            


Solution().romanToInt("MMMDCCCLXXXVIII")