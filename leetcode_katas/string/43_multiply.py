class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = ""
        postfix_zeroes_qty = 0

        for i in range(len(num2)-1, -1, -1):
            curr = ""
            remainder = 0    

            for j in range(len(num1)-1, -1, -1):
                mul = int(num2[i]) * int(num1[j]) + remainder
                curr = str(mul % 10) + curr
                remainder = mul // 10

            if remainder:    
                curr = str(remainder) + curr

            curr = curr + ("0" * postfix_zeroes_qty)

            if not res:
                res = curr
            else:
                res = str(int(res) + int(curr))     

            postfix_zeroes_qty += 1

        return res

    
Solution().multiply("999", "999")