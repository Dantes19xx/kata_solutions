# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = head

        if head is None:
            return None

        if head.next is None:
            return head

        curr_node = temp
        while curr_node and curr_node.next:
           
            next_node = curr_node.next

            if curr_node.val == next_node.val:
                curr_node.next = next_node.next
            
            else:
                curr_node = curr_node.next

        return head