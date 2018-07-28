# Merge two sorted list
#

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def merge_two_sorted_list(L1, L2):
    head = tail = ListNode()

    # save head
    if L1.data < L2.data:
        head = L1
    else:
        head = L2
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        
        tail = tail.next
    
    if L1 != None:
        tail.next = L1
    elif L2 != None:
        tail.next = L2

    return head

def traverse(L):
    while L:
        print(L.data)
        L = L.next

def main():
    i1, i2, i3, i4, i5, i6 = ListNode(1), ListNode(3), ListNode(5), ListNode(8), ListNode(9), ListNode(14)
    i1.next, i2.next, i3.next, i4.next, i5.next = i2, i3, i4, i5, i6

    j1, j2, j3, j4 = ListNode(2), ListNode(7), ListNode(22), ListNode(33)
    j1.next, j2.next, j3.next = j2, j3, j4

    r = merge_two_sorted_list(i1, j1)
    traverse(r)

if __name__ == '__main__':
    main()



