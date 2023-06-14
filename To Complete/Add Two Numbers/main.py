# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def addTwoNumbers(l1, l2):
    sum = 0
    num1 = str(l1)
    while l1.next != None:
        num1 += str(l1)
        l1 = l1.next
    return num1

addTwoNumbers([1, 2, 3, 4], [1, 2, 3, 4])