# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
def add_two_nums(l1, l2):
    if l1 is None and l2 is not None:
        return l2
    elif l1 is not None and l2 is None:
        return l1
    elif l1 is None and l2 is None:
        return None

    result, current = None, None
    carry = 0
    while l1 is not None or l2 is not None:
        first_data = 0 if l1 is None else l1.data
        second_data = 0 if l2 is None else l2.data
        sum = first_data + second_data + carry
        new_node = Node()
        if sum < 10:
            new_node.data = sum
            carry = 0
        else:
            new_node.data = sum % 10
            carry = 1

        if result is None:
            result = new_node
            current = result
        else:
            current.next = new_node
            current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if carry > 0:
        current.next = Node(carry)
    return result

def print_result(l):
    while l is not None:
        print(l.data)
        l = l.next
    print('')

if __name__ == '__main__':
    n1 = Node(3)
    n2 = Node(5, n1)
    n3 = Node(6, n2)
    m1 = Node(1)
    m2 = Node(7, m1)
    m3 = Node(8, m2)
    m4 = Node(9, m3)
    print_result(add_two_nums(n3, m4))

    n1 = Node(5)
    m1 = Node(5)
    print_result(add_two_nums(n1, m1))

    n1 = Node(9)
    n2 = Node(9, n1)
    m1 = Node(1)
    print_result(add_two_nums(n2, m1))


