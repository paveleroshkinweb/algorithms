def shiftLinkedList(head, k):
    assert head is not None
    l = length(head)
    k = k % l
    if k == 0:
        return head
    return shift_forward(head, k, l)


def shift_forward(head, k, l):
    index = 0
    last = head
    prev = None
    while last.next:
        if index == l - k:
            prev = last
        last = last.next
        index += 1
    prev = prev or last
    current = head
    while current.next is not prev:
        last.next = current
        current = current.next
        last = last.next
    last.next = current
    current.next = None
    return prev


def length(head):
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    return length

