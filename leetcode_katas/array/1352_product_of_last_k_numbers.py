class ProductOfNumbers(object):

    def __init__(self):
        self.arr = []
        self.prefix = [1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """

        if num == 0:
            self.prefix = [1]
        
        else:
            self.prefix.append(num * self.prefix[-1])

        self.arr.append(num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """

        if k >= len(self.prefix):
            return 0
        
        else: 
            return self.prefix[-1] // self.prefix[len(self.prefix) - k - 1]

            
        


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.arr)
print(obj.getProduct(2)) #20
print(obj.getProduct(3)) #40
print(obj.getProduct(4)) #0
# obj.add(num)
# param_2 = obj.getProduct(k)