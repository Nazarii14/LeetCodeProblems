def addTwoNumbers(l1, l2):
    head = ListNode()
    current = head
    carry = 0

    while (l1 != None or l2 != None or carry != 0):
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        total = l1_value + l2_value + carry
        current.next = ListNode(total % 10)
        carry = total // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        current = current.next
    return head.next
