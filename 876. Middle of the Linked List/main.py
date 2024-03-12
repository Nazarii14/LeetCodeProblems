class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    m1 = head
    lst = []

    while m1.next:
        lst += m1.value
        m1 = m1.next

    if len(lst) % 2 == 0:
        return lst[len(lst)//2:]
    else:
        return lst[len(lst)//2+1:]


