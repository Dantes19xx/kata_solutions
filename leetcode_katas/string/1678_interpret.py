class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        res = ""
        substr = ""

        for ch in command:
            if ch == "(":
                substr += "("
            elif ch == ")":
                if substr == "(":
                    res += "o"
                else:
                    res += "al"
                
                substr = ""
            else:
                if substr:
                    substr += ch
                else:
                    res += ch
            
        return res

Solution().interpret("(al)G(al)()()G")