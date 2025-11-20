class Solution(object):
    def multiply(self, num1, num2):
        n1 = 0
        for i in num1:
           n1=n1*10 + int(i)

        n2 = 0
        for j in num2:
            n2 = n2*10+int(j)
        return str(n1*n2)  

    
Solution().multiply("123", "456")