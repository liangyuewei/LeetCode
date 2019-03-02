# Given a linked list, swap every two adjacent nodes and return its head.
# Example:
#   Given 1->2->3->4, you should return the list as 2->1->4->3.
class Solution(object):
    def swap_nodes_in_pairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
            