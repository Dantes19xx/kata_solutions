# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def recur(visited, hB):
            if not hB:
                return None
            
            if hB in visited:
                return hB
            
            return recur(visited, hB.next)


        visites_nodes = set() # set предпочтительнее, у него скорость поиска O(1)

        skipA = headA
        skipB = headB

        while skipA:
            visites_nodes.add(skipA)
            skipA = skipA.next

        return recur(visites_nodes, skipB)
    