class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        
        n = len(friends) - 1
        friends_faced = 0
        i = 0
        res = []

        while friends_faced <= n:
            if order[i] in friends:
                res.append(order[i])
                friends_faced += 1
            i += 1

        return res

Solution().recoverOrder([1,4,5,3,2], [2,5])