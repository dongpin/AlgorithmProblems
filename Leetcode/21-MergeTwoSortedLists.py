# 21. Merge two sorted lists
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#

class ListNode():
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    head = current = None
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            if head is None:
                head = current = ListNode(l1.val)
            else:
                current.next = ListNode(l1.val)
                current = current.next
            l1 = l1.next
        else:
            if head is None:
                head = current = ListNode(l2.val)
            else:
                current.next = ListNode(l2.val)
                current = current.next
            l2 = l2.next
        
    if l1 is None:
        while l2 is not None:
            current.next = ListNode(l2.val)
            current = current.next
            l2 = l2.next
    if l2 is None:
        while l1 is not None:
            current.next = ListNode(l1.val)
            current = current.next
            l1 = l1.next

    return head
        
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next, n2.next = n2, n3

    m1 = ListNode(1)
    m2 = ListNode(3)
    m3 = ListNode(4)
    m1.next, m2.next = m2, m3

    result = merge_two_lists(n1, m1)
    while result is not None:
        print(result.val)
        result = result.next

