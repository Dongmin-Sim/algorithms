def reverseList(head):
    node, prev = head, None

    while node:
        temp, node.next = node.next, prev
        prev, node = node, temp 

    return prev