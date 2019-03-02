# Reverse a singly linked list.
# Example:
#   Input: 1->2->3->4->5->NULL
#   Output: 5->4->3->2->1->NULL

class Solution(object):
    def reverse_linked_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev