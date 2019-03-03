class Solution(object):
    def linked_list_cycle(self, head):
        fast = slow = head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False