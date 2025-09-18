
class NewNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = NewNode(data)
        new_node.next = None
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while new_node is not None:
                if temp.next is None:
                    temp.next = new_node
                    new_node = None
                temp = temp.next



    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return
        
        prev = None
        
        while temp:
            while temp and temp.data != key:
                prev = temp
                temp = temp.next

            if temp:
                prev.next = temp.next

            temp = temp.next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        l_list = self.fill_linked_list(head)
        l_list.delete(val)

        return l_list

    def fill_linked_list(self, head):
        
        l_list = LinkedList()

        for i in head:
            l_list.push(i)

           
        return l_list
    



print(Solution().removeElements([1,2,6,3,4,5,6], 6))