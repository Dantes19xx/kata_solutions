from collections import deque


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        self.head_len = len(head)
        pivot_idx = self.get_pivot_idx()
        is_odd_head_len = self.is_odd_head_len()

        d = deque()

        for i in range(self.head_len):
            if i <= pivot_idx:
                d.appendleft(head[i])
            
            elif i == pivot_idx + 1 and is_odd_head_len:
                d.popleft()

            elif i > pivot_idx:
                if head[i] == d[0]:
                    d.popleft()

                else:
                    return False
        
        if is_odd_head_len and d[0] == head[-1]:
            d.popleft()
            
        if not len(d):
            return True
        
        return False

    
    def get_pivot_idx(self):
        if self.head_len % 2 == 0:
            return (self.head_len // 2) - 1
        
        return self.head_len // 2
    
    def is_odd_head_len(self):
        return self.head_len % 2 == 1




# [1,2,2,1]
Solution().isPalindrome([2, 2, 1])

[1,2,2,1,2]